from argparse import ArgumentParser, Namespace
from bz2 import BZ2File
from functools import reduce
from gzip import GzipFile
from itertools import count, islice
from lzma import LZMAFile
from math import ceil, floor, log, log2
from pathlib import Path
from struct import pack, unpack
from sys import stdin, stdout
from typing import IO, Generator, Literal, Optional, Tuple, Union, overload

import numpy as np

from tqdm import tqdm

from . import GenProto
from .compat.fluidpythran import boost
from .compat.itertools import batched

start_string = 'The Thue-Morse sequence for {} Players{}, Definition {:02}, up to {} is: '
struct_format = ">?BHQ"  # (kind == '2', def - 1, players - 2, entries - 1)
struct_size = 12


@boost
def np_select_type(n: int) -> 'np.typing.DTypeLike':
    error = "Your base is too large to support efficiently (max is {})"
    for threshhold, t, message in (
        (2, np.uint8, "Doesn't support unary or negative bases"),
        (1 << 7, np.uint8, ""),
        (1 << 15, np.uint16, ""),
        (1 << 31, np.uint32, ""),
        (1 << 63, np.uint64, ""),
        (1 << 127, getattr(np, "uint128", None), error.format((1 << 63) - 1)),
        (1 << 255, getattr(np, "uint256", None), error.format((1 << 127) - 1)),
    ):
        if n < threshhold:
            if t is None:
                raise ValueError(message)
            return t
    raise ValueError(f"Your base is too large to support efficiently (max is {(1 << 255) - 1})")


def min_bytes_batch(base: int) -> Tuple[int, int, int]:
    bits_per_entry = ceil(log2(base))
    for k in count(1):
        total_bits = bits_per_entry * k
        if total_bits % 8 == 0:
            return int(k), int(bits_per_entry), int(total_bits // 8)
    return -1, -1, -1


def human_readable_bytes(byte_size):
    units = ["B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB"]
    if byte_size == 0:
        return "0 B"

    power = int(floor(log(byte_size, 1024)))
    size_in_unit = byte_size / (1024 ** power)
    return f"{size_in_unit:.1f} {units[power]}"


@boost
def run(
    num: int,
    func: Optional[GenProto],
    kind: str = '2',
    from_file: bool = False
) -> None:
    parser = ArgumentParser()
    parser.add_argument('n', type=int, help='The number of values to print', default=16, nargs='?')
    parser.add_argument('p', type=int, help='The number of players', default=2, nargs='?')
    if not from_file:
        parser.add_argument('--to-file', type=str, dest='file', help='Optionally, the file to dump this sequence to',
                            default='stdout', nargs='?')
        parser.add_argument('-q', dest='quiet', help='If in file mode, set this to not print progress', default=False,
                            action='store_true')
    else:
        parser.add_argument('--from-file', type=str, dest='file', default='stdin', nargs='?',
                            help='Optionally, the file to read this sequence from')

    args = parser.parse_args()
    if kind == '2':
        kind_str = ''
    else:
        kind_str = f' ({args.p} selected)'

    if from_file:
        process_file_input(args)
    else:
        assert func is not None
        if args.file == 'stdout':
            print(start_string.format(kind, kind_str, num, args.n), end='')
            stdout.flush()
            for x in islice(func(args.p), args.n):
                print(x, "", end='')
            print()
        else:
            process_file_output(args, func, kind, kind_str, num)


@boost
def get_file_obj(
    fname: str,
    mode: Literal['r', 'rb', 'w', 'wb', 'a', 'ab', 'x', 'xb']
) -> Union[BZ2File, GzipFile, LZMAFile, IO[bytes]]:
    pname = Path(fname)
    if fname.endswith('.bz'):
        return BZ2File(fname, mode)
    if fname.endswith('.gz'):
        return GzipFile(pname, mode)
    if fname.endswith('.lz'):
        return LZMAFile(pname, mode)
    return pname.open(mode)


@overload
def process_file_input(args: Namespace, gen_mode: Literal[True]) -> Generator[int, None, None]:
    ...


@overload
def process_file_input(args: Namespace, gen_mode: Literal[False] = False) -> None:
    ...


@boost
def process_file_input(args: Namespace, gen_mode: bool = False):
    if args.file == 'stdin':
        f_obj = stdin.buffer
    else:
        f_obj = get_file_obj(args.file, 'rb')

    try:
        _kind, def_, p, entries = unpack(struct_format, f_obj.read(struct_size))
        kind = '2' if _kind else 'n'
        def_ += 1
        entries += 1
        p += 2
        batch_size, bits_per_entry, batch_bytes = min_bytes_batch(p)
        buff = f_obj.read(batch_bytes)
        kind_str = f' ({p} selected)' * (not _kind)

        if not gen_mode:
            print(start_string.format(kind, kind_str, def_, entries), end='')
        while buff:
            batch = []
            buff_val = int.from_bytes(buff, 'big')
            while buff_val:
                batch.append(buff_val & ((1 << bits_per_entry) - 1))
                buff_val >>= bits_per_entry
            batch += [0] * (batch_size - len(batch))
            if gen_mode:
                yield from batch
            else:
                print(" ".join(str(x) for x in batch), end='')
            buff = f_obj.read(batch_bytes)
    finally:
        if f_obj is not stdin.buffer:
            f_obj.close()


@boost
def process_file_output(
    args: Namespace,
    func: GenProto,
    kind: str,
    kind_str: str,
    num: int
) -> None:
    print("Dumping compact output to", args.file)
    batch_size, bits_per_entry, batch_bytes = min_bytes_batch(args.p)
    total_bytes = args.n * batch_bytes / batch_size + struct_size

    if total_bytes > (1 << 30):
        print(f"Warning: attempting to write {human_readable_bytes(total_bytes)}")

    if not args.quiet:
        print(start_string.format(kind, kind_str, num, args.n), end='')
    else:
        print(f"Selected p{kind}_d{num:02} for {args.n} entries ({human_readable_bytes(total_bytes)})")
    stdout.flush()

    with get_file_obj(args.file, 'wb') as f:
        f.write(pack(struct_format, kind == '2', num - 1, args.p - 2, args.n - 1))
        for group in tqdm(
            batched(zip(range(args.n), func(args.p, args.n)), batch_size),
            total=args.n // batch_size,
            disable=not args.quiet,
            file=stdout
        ):
            batch = [y for _, y in group]

            if not args.quiet:
                for x in batch:
                    print(x, "", end='')

            if len(batch) != batch_size:
                batch += [0] * (batch_size - len(batch))
            to_write = reduce(
                lambda x, y: (x << bits_per_entry) + y,
                reversed(batch)
            ).to_bytes(batch_bytes, 'big')
            f.write(to_write)
        f.flush()
