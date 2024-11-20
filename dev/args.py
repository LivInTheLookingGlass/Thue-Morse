from argparse import ArgumentParser
from functools import reduce
from itertools import count
from math import ceil, floor, log, log2
from pathlib import Path
from sys import stdout
from typing import Callable, Generator, Tuple

import numpy as np

from .compat.fluidpythran import boost
from .compat.itertools import batched


@boost
def np_select_type(n: int) -> 'np.typing.DTypeLike':
    if n < 2:
        raise ValueError("Doesn't support unary or negative bases")
    if n < (1 << 7):
        return np.uint8
    if n < (1 << 15):
        return np.uint16
    if n < (1 << 31):
        return np.uint32
    if n < (1 << 63):
        return np.uint64
    try:
        if n < (1 << 127):
            return np.uint128
    except AttributeError:  # np.uint128 and higher is conditionally supported
        raise ValueError(f"Your base is too large to support efficiently (max is {(1 << 63) - 1})")
    try:
        if n < (1 << 255):
            return np.uint256
    except AttributeError:  # np.uint256 is conditionally supported
        raise ValueError(f"Your base is too large to support efficiently (max is {(1 << 127) - 1})")
    raise ValueError(f"Your base is too large to support efficiently (max is {(1 << 255) - 1})")


def min_bytes_batch(base: int) -> Tuple[int, int, int]:
    bits_per_entry = ceil(log2(base))
    for k in count(1):
        total_bits = bits_per_entry * k
        if total_bits % 8 == 0:
            return int(k), int(bits_per_entry), int(total_bits // 8)


def human_readable_bytes(byte_size):
    units = ["B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB"]
    if byte_size == 0:
        return "0 B"

    power = int(floor(log(byte_size, 1024)))
    size_in_unit = byte_size / (1024 ** power)
    return f"{size_in_unit:.1f} {units[power]}"


@boost
def run(num: int, func: Callable[[int], Generator[int, None, None]], kind: str = '2') -> None:
    parser = ArgumentParser()
    parser.add_argument('n', type=int, help='The number of values to print', default=16, nargs='?')
    parser.add_argument('p', type=int, help='The number of players', default=2, nargs='?')
    parser.add_argument('--to-file', type=str, dest='file', help='Optionally, the file to dump this sequence to', default='stdout', nargs='?')
    parser.add_argument('-q', dest='quiet', help='If in file mode, set this to not print progress', default=False, action='store_true')
    args = parser.parse_args()
    if kind == '2':
        kind_str = ''
    else:
        kind_str = f' ({args.p} selected)'

    start_string = f'The Thue-Morse sequence for {kind} Players{kind_str}, Definition {num:02}, up to {args.n} is: '
    if args.file == 'stdout':
        print(start_string, end='')
        stdout.flush()
        for x, _ in zip(func(args.p), range(args.n)):
            print(x, "", end='')
        print()

    else:
        print("Dumping compact output to", args.file)
        batch_size, bits_per_entry, batch_bytes = min_bytes_batch(args.p)
        total_bytes = args.n * batch_bytes / batch_size

        if total_bytes > (1 << 30):
            print(f"Warning: attempting to write {human_readable_bytes(total_bytes)}")

        if not args.quiet:
            print(start_string, end='')
        else:
            print(f"Selected p{kind}_d{num:02} for {args.n} entries ({human_readable_bytes(total_bytes)})")
        stdout.flush()

        with Path(args.file).open('wb') as f:
            for group in batched(zip(range(args.n), func(args.p)), batch_size):
                batch = [y for _, y in group]
                if len(batch) != batch_size:
                    batch += [0] * (batch_size - len(batch))

                if not args.quiet:
                    for x in batch:
                        print(x, "", end='')
                else:
                    print(f"{group[-1][0] + 1} of {args.n}...\r")
                stdout.flush()

                to_write = reduce(
                    lambda x, y: (x << bits_per_entry) + y,
                    reversed(batch)
                ).to_bytes(batch_bytes, 'big')
                f.write(to_write)
                f.flush()
