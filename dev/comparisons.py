from argparse import Namespace
from atexit import register
from enum import Enum, auto
from itertools import chain, count
from logging import INFO, FileHandler, StreamHandler, basicConfig, getLogger, shutdown
from pathlib import Path
from shelve import Shelf
from shelve import open as shelf_open

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

p2_defs = [int(p.name[1:-3]) for p in Path(__file__).parent.glob('p2/d*.py')]
pn_defs = [int(p.name[1:-3]) for p in Path(__file__).parent.glob('pn/d*.py')]
pn_defs.remove(1)
all_defs = [('2', d) for d in p2_defs] + [('n', d) for d in pn_defs]


class Operation(Enum):
    DUMP = auto()
    COMPARE = auto()
    CLEAN = auto()


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
        pending_loop(shelf)


@boost
def begin(shelf: Shelf) -> None:
    stop = shelf['stop']
    base_stop = shelf['base_stop']
    shelf['next_operation'] = (Operation.DUMP, ('n', 1, 2, stop))
    task_list = list(chain.from_iterable(
        [(Operation.DUMP, (kind, def_, 2, stop)), (Operation.COMPARE, (('n', 1, 2, stop, kind, def_)))]
        for kind, def_ in all_defs
    ))
    task_list.append((Operation.CLEAN, (2, )))
    for base in range(3, base_stop):
        task_list.append((Operation.DUMP, ('n', 1, base, stop)))
        task_list.extend(chain.from_iterable(
            [(Operation.DUMP, ('n', def_, base, stop)), (Operation.COMPARE, (('n', 1, base, stop, 'n', def_)))]
            for def_ in pn_defs
        ))
        task_list.append((Operation.CLEAN, (base, )))
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
        else:
            error_str = f"Unknown next operation: ({next_op}, {params})"
            logger.error(error_str)
            raise ValueError(error_str)

        # set up next op
        if shelf['pending']:
            shelf['next_operation'], *shelf['pending'] = shelf['pending']
        else:
            shelf['next_operation'] = None
        shelf.sync()


@boost
def handle_dump(kind: str, def_: int, base: int, stop: int) -> None:
    args = Namespace()
    args.n = stop
    args.p = base
    args.file = f'work/p{kind}.d{def_:02}.{base}.{stop}.bin.gz'
    args.quiet = True
    if kind == 'n':
        kind_str = f' ({def_} selected)'
    else:
        kind_str = ''
    process_file_output(args, get_iters(f'p{kind}.d{def_:02}')[0], kind, kind_str, def_)


@boost
def handle_clean(base: int) -> None:
    for f in Path('work').glob(f'*.*.{base}.*.bin*'):
        f.unlink(missing_ok=True)


@boost
def handle_compare(kind1: str, def1: int, base: int, stop: int, kind2: str, def2: int) -> None:
    chunk_size = 1 << 20
    fname1 = f'work/p{kind1}.d{def1:02}.{base}.{stop}.bin.gz'
    fname2 = f'work/p{kind2}.d{def2:02}.{base}.{stop}.bin.gz'
    with get_file_obj(fname1, 'rb') as f1, get_file_obj(fname2, 'rb') as f2:
        f1.seek(struct_size)
        f2.seek(struct_size)

        chunk1 = f1.read(chunk_size - struct_size)
        chunk2 = f2.read(chunk_size - struct_size)
        if chunk1 != chunk2:
            error_str = f"Files differ in first chunk of {chunk_size} bytes"
            logger.error(error_str)
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
    Path(fname2).unlink()


if __name__ == '__main__':
    main()
