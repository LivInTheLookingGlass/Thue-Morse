from argparse import ArgumentParser, Namespace
from atexit import register
from enum import Enum, auto
from itertools import chain
from logging import INFO, FileHandler, StreamHandler, basicConfig, getLogger, shutdown
from multiprocessing import Process
from multiprocessing.shared_memory import SharedMemory
from pathlib import Path
from shelve import Shelf
from shelve import open as shelf_open
from struct import error as StructError
import sys
from time import sleep
from typing import Dict, List, Literal, Tuple, Union

from tqdm import tqdm

from . import get_iters
from .args import process_file_input, process_file_output
from .compat.fluidpythran import boost

basicConfig(
    level=INFO,
    format='[%(asctime)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        StreamHandler(),
        FileHandler('comparisons.log', mode='a')
    ]
)
logger = getLogger(__name__)
register(shutdown)

p2_defs = sorted(int(p.name[1:-3]) for p in Path(__file__).parent.glob('p2/d*.py'))
pn_defs = sorted(int(p.name[1:-3]) for p in Path(__file__).parent.glob('pn/d*.py'))
pn_defs.remove(1)
all_defs = [('2', d) for d in p2_defs] + [('n', d) for d in pn_defs]
always_spin_off = [  # rough order of slowest to fastest
    ('2', 15),
    ('n', 9),
    ('2', 17),
    ('n', 2),
    ('n', 5),
    ('2', 5),
    ('n', 6),
    ('n', 7),
    ('2', 3),
]
truncated_defs = [  # these don't have enough precision in python to give full sequence
    ('2', 18),
    ('2', 19),
    ('2', 20),
]


class Operation(Enum):
    DUMP = auto()
    COMPARE = auto()
    CLEAN = auto()
    SPINOFF = auto()
    AWAIT = auto()


DUMP_TYPE = Tuple[str, int, int, int]
COMPARE_TYPE = Tuple[str, int, int, int, str, int]
CLEAN_TYPE = Tuple[int]
SPINOFF_AWAIT_TYPE = Union[
    Tuple[Literal[Operation.DUMP], DUMP_TYPE],
    Tuple[Literal[Operation.COMPARE], COMPARE_TYPE],
    Tuple[Literal[Operation.CLEAN], CLEAN_TYPE]
]
ANY_JOB_TYPE = Union[
    SPINOFF_AWAIT_TYPE,
    Tuple[Literal[Operation.SPINOFF, Operation.AWAIT], SPINOFF_AWAIT_TYPE]
]
tasks: Dict[Tuple[Literal[Operation.SPINOFF], SPINOFF_AWAIT_TYPE], Tuple[SharedMemory, Process]] = {}


def get_fname(kind: str, def_: int, base: int, stop: int) -> str:
    return f'work/p{kind}.d{def_:02}.{base}.{stop}.bin.gz'


@boost
def main(stop: int = (1 << 16), base_stop: int = 257, forked: bool = False) -> None:
    Path('work').mkdir(exist_ok=True)
    with shelf_open('work/comparisons.pickle') as shelf:
        stop = shelf.get('stop', stop)
        shelf['stop'] = stop
        shelf['forked'] = forked
        base_stop = shelf.get('base_stop', base_stop)
        shelf['base_stop'] = base_stop
        if shelf.get('next_operation') is None:
            begin(shelf)
        for job in shelf.get('spun_off', ()):
            handle_spinoff(shelf, job)
        pending_loop(shelf)


@boost
def begin(shelf: Shelf) -> None:
    stop: int = shelf['stop']
    base_stop: int = shelf['base_stop']
    shelf['next_operation'] = (Operation.SPINOFF, (Operation.DUMP, ('n', 1, 2, stop)))
    task_list: List[ANY_JOB_TYPE] = []
    new_list: List[ANY_JOB_TYPE] = []
    aso = always_spin_off if not shelf['forked'] else [d for d in reversed(all_defs) if d not in truncated_defs]
    for kind, def_ in aso:
        task_list.append((Operation.SPINOFF, (Operation.DUMP, (kind, def_, 2, stop))))
        new_list.append((Operation.COMPARE, ('n', 1, 2, stop, kind, def_)))
        new_list.append((Operation.AWAIT, (Operation.DUMP, (kind, def_, 2, stop))))
    insert_spot = len(task_list) + 1
    task_list.extend(chain.from_iterable(
        [(Operation.DUMP, (kind, def_, 2, stop)), (Operation.COMPARE, (('n', 1, 2, stop, kind, def_)))]
        for kind, def_ in all_defs
        if ((kind, def_) not in aso and (kind, def_) not in truncated_defs)
    ))
    task_list.insert(insert_spot, (Operation.AWAIT, (Operation.DUMP, ('n', 1, 2, stop))))
    task_list.extend(reversed(new_list))
    task_list.append((Operation.CLEAN, (2, )))
    for base in range(3, base_stop):
        new_list = []
        new_new_list: List[ANY_JOB_TYPE] = []
        new_list.append((Operation.SPINOFF, (Operation.DUMP, ('n', 1, base, stop))))
        for idx, (kind, def_) in enumerate(aso, start=1):
            if kind == '2':
                continue
            new_list.insert(idx * 2 + 1, (Operation.SPINOFF, (Operation.DUMP, (kind, def_, base, stop))))
            new_new_list.append((Operation.COMPARE, ('n', 1, base, stop, kind, def_)))
            new_new_list.append((Operation.AWAIT, (Operation.DUMP, (kind, def_, base, stop))))
        insert_spot = len(new_list) + 1
        new_list.extend(chain.from_iterable(
            [(Operation.DUMP, ('n', def_, base, stop)), (Operation.COMPARE, (('n', 1, base, stop, 'n', def_)))]
            for def_ in pn_defs
            if (('n', def_) not in aso and ('n', def_) not in truncated_defs)
        ))
        new_list.insert(insert_spot, (Operation.AWAIT, (Operation.DUMP, ('n', 1, base, stop))))
        new_list.extend(reversed(new_new_list))
        new_list.append((Operation.CLEAN, (base, )))
        task_list.extend(new_list)
    shelf['pending'] = task_list
    shelf.sync()


@boost
def pending_loop(shelf: Shelf) -> None:
    while shelf['next_operation'] or shelf['pending']:
        next_op, params = shelf['next_operation']
        # process current op
        if next_op == Operation.DUMP:
            logger.info("Dumping: kind={}, def={}, base={}, stop={}".format(*params))
            handle_dump(*params)
        elif next_op == Operation.COMPARE:
            logger.info("Comparing: base={2}, stop={3}, kind1={0}, def1={1}, kind2={4}, def2={5}".format(*params))
            handle_compare(*params)
        elif next_op == Operation.CLEAN:
            logger.info("Cleaning up base {}".format(*params))
            handle_clean(*params)
        elif next_op == Operation.SPINOFF:
            logger.info("Spinning off task: {}".format(params))
            handle_spinoff(shelf, params)
        elif next_op == Operation.AWAIT:
            logger.info("Awaiting task: {}".format(params))
            handle_await(shelf, params)
        else:
            error_str = f"Unknown next operation: ({next_op}, {params})"
            logger.error(error_str)
            raise ValueError(error_str)

        # set up next op
        shelf['next_operation'], *shelf['pending'] = shelf.get('pending') or [None]
        shelf.sync()


@boost
def handle_dump(kind: str, def_: int, base: int, stop: int) -> None:
    args = Namespace()
    args.n = stop
    args.p = base
    args.file = get_fname(kind, def_, base, stop)
    args.quiet = True
    if kind == 'n':
        kind_str = f' ({def_} selected)'
    else:
        kind_str = ''
    process_file_output(args, get_iters(f'p{kind}.d{def_:02}')[0], kind, kind_str, def_)
    logger.info("Dump Complete: kind={}, def={}, base={}, stop={}".format(kind, def_, base, stop))


@boost
def handle_clean(base: int) -> None:
    for f in Path('work').glob(f'*.*.{base}.*.bin*'):
        f.unlink(missing_ok=True)


@boost
def handle_compare(kind1: str, def1: int, base: int, stop: int, kind2: str, def2: int) -> None:
    fname1 = get_fname(kind1, def1, base, stop)
    fname2 = get_fname(kind2, def2, base, stop)
    for attempt in [1, 2]:
        try:
            for idx, (v1, v2) in tqdm(enumerate(zip(
                process_file_input(Namespace(file=fname1), True),
                process_file_input(Namespace(file=fname2), True))
            ), total=stop, file=sys.stdout, dynamic_ncols=True):
                if v1 != v2:
                    raise ValueError(f"Mismatch at T({idx})! {v1} ≠ {v2}")
            break
        except (FileNotFoundError, StructError, ValueError) as e:
            error_str = f"Error: {e.args}"
            logger.error(error_str)
            if attempt == 1:
                logger.info("Trying again in 5 seconds")
                sleep(5)
                continue
            else:
                raise


@boost
def spinoff_worker(output: str, job: Tuple[Operation, Tuple]) -> None:
    try:
        shared_mem = SharedMemory(name=output)

        def write(message: str):
            shared_mem.buf[:] = message.rstrip('\r').encode().ljust(shared_mem.size, b'\00')

        def flush(*args, **kwargs):
            pass

        # this is a hack, but it works
        sys.stdout.write = write  # type: ignore
        sys.stdout.flush = flush  # type: ignore

        task, params = job
        if task == Operation.DUMP:
            handle = handle_dump
        else:
            error_str = f"Spinning off non-dumps not yet supported. Got: {job}"
            logger.error(error_str)
            raise ValueError(error_str)

        handle(*params)
    finally:
        shared_mem.close()


@boost
def handle_spinoff(shelf: Shelf, job: Tuple[Literal[Operation.SPINOFF], SPINOFF_AWAIT_TYPE]) -> None:
    output = SharedMemory(create=True, size=(1 << 16))
    p = Process(
        target=spinoff_worker,
        args=(output.name, job)
    )
    tasks[job] = (output, p)
    if 'spun_off' not in shelf:
        shelf['spun_off'] = [job]
    else:
        shelf['spun_off'].append(job)
    shelf.sync()
    p.start()


@boost
def handle_await(shelf: Shelf, job: Tuple[Literal[Operation.SPINOFF], SPINOFF_AWAIT_TYPE]) -> None:
    output, p = tasks[job]
    while p.is_alive():
        print(output.buf.tobytes().strip(b'\x00').decode(), end='\r')
        sys.stdout.flush()
        sleep(0.1)
    p.join()
    if p.exitcode:
        error_str = f'Child process failed! Exit code {p.exitcode} on {job}'
        logger.error(error_str)
        raise RuntimeError(error_str)
    del tasks[job]
    output.close()
    output.unlink()
    if job in shelf.get('spun_off', []):
        shelf['spun_off'].remove(job)
        shelf.sync()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('n', type=int, help='The number of values to test', default=(1 << 15), nargs='?')
    parser.add_argument('p', type=int, help='The maximum number of players to test against', default=256, nargs='?')
    parser.add_argument('-f', '--fork-all', action='store_true', help='If given, this flag will force the runner to spin off all tasks possible, rather than running some serially', dest='forked')
    parser.add_argument('--exclude', type=str, help='exclude the given definitions or definition ranges. Format as 2_01 or n_01-07', action='append')
    parser.add_argument('--include', type=str, help='only run the given definitions or definition ranges. Format as 2_01 or n_01-07', action='append')

    args = parser.parse_args()
    main(args.n, args.p + 1, args.forked)
