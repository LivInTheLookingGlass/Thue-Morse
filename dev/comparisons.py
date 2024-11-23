from argparse import Namespace
from atexit import register
from enum import Enum, auto
from itertools import chain, count
from logging import INFO, FileHandler, StreamHandler, basicConfig, getLogger, shutdown
from multiprocessing import Process
from multiprocessing.shared_memory import SharedMemory
from pathlib import Path
from shelve import Shelf
from shelve import open as shelf_open
from sys import stdout
from time import sleep
from typing import Dict, List, Literal, Tuple, Union

from . import get_iters
from .args import get_file_obj, process_file_output, struct_size
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
always_spin_off = [('n', 1), ('2', 13), ('2', 15), ('n', 9)]


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
def main(stop: int = (1 << 16), base_stop: int = 257) -> None:
    Path('work').mkdir(exist_ok=True)
    with shelf_open('work/comparisons.pickle') as shelf:
        stop = shelf.get('stop', stop)
        shelf['stop'] = stop
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
    task_list: List[ANY_JOB_TYPE] = list(chain.from_iterable(
        [(Operation.DUMP, (kind, def_, 2, stop)), (Operation.COMPARE, (('n', 1, 2, stop, kind, def_)))]
        for kind, def_ in all_defs
        if (kind, def_) not in always_spin_off
    ))
    task_list.insert(1, (Operation.AWAIT, (Operation.DUMP, ('n', 1, 2, stop))))
    for idx, (kind, def_) in enumerate(always_spin_off, start=1):
        task_list.insert(idx * 2 + 1, (Operation.SPINOFF, (Operation.DUMP, (kind, def_, 2, stop))))
        task_list.append((Operation.AWAIT, (Operation.DUMP, (kind, def_, 2, stop))))
        task_list.append((Operation.COMPARE, ('n', 1, 2, stop, kind, def_)))
    task_list.append((Operation.CLEAN, (2, )))
    for base in range(3, base_stop):
        new_list: List[ANY_JOB_TYPE] = []
        new_list.append((Operation.SPINOFF, (Operation.DUMP, ('n', 1, base, stop))))
        new_list.extend(chain.from_iterable(
            [(Operation.DUMP, ('n', def_, base, stop)), (Operation.COMPARE, (('n', 1, base, stop, 'n', def_)))]
            for def_ in pn_defs
            if ('n', def_) not in always_spin_off
        ))
        new_list.insert(1, (Operation.AWAIT, (Operation.DUMP, ('n', 1, base, stop))))
        for idx, (kind, def_) in enumerate(always_spin_off, start=1):
            if kind == '2':
                continue
            new_list.insert(idx * 2 + 1, (Operation.SPINOFF, (Operation.DUMP, (kind, def_, base, stop))))
            new_list.append((Operation.AWAIT, (Operation.DUMP, (kind, def_, base, stop))))
            new_list.append((Operation.COMPARE, ('n', 1, base, stop, kind, def_)))
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
        shelf['next_operation'], *shelf['pending'] = shelf.get('pending', [None])
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
    chunk_size = 1 << 20
    fname1 = get_fname(kind1, def1, base, stop)
    fname2 = get_fname(kind2, def2, base, stop)
    for attempt in [1, 2]:
        with get_file_obj(fname1, 'rb') as f1, get_file_obj(fname2, 'rb') as f2:
            f1.seek(struct_size)
            f2.seek(struct_size)

            chunk1 = f1.read(chunk_size - struct_size)
            chunk2 = f2.read(chunk_size - struct_size)
            if chunk1 != chunk2:
                error_str = f"Files differ in first chunk of {chunk_size} bytes"
                logger.error(error_str)
                if attempt == 1:
                    logger.info("Trying again in 5 seconds")
                    sleep(5)
                    continue
                raise ValueError(error_str)

            for idx in count(1):
                chunk1 = f1.read(chunk_size)
                chunk2 = f2.read(chunk_size)

                if not chunk1 and not chunk2:
                    logger.info("Compare success! No difference in output")
                    break  # Files match

                if chunk1 != chunk2:
                    error_str = f"Files differ at chunk {idx} (chunk size = {chunk_size})"
                    logger.error(error_str)
                    raise ValueError(error_str)
        break
    Path(fname2).unlink()


@boost
def spinoff_worker(output: str, job: Tuple[Operation, Tuple]) -> None:
    import sys
    try:
        shared_mem = SharedMemory(name=output)

        def write(message: str):
            shared_mem.buf[:] = message.rstrip('\r').encode().ljust(shared_mem.size, b'\00')

        # this is a hack, but it works
        sys.stdout.write = write  # type: ignore

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
        stdout.flush()
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
    main()
