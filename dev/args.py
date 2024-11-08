from argparse import ArgumentParser
from typing import Callable, Iterable

try:
    from butarray import bitarray
except ImportError:
    bitarray = bytearray  # type: ignore


def run(num: int, func: Callable[[int], Iterable[int]], kind: str = '2') -> None:
    parser = ArgumentParser()
    parser.add_argument('n', type=int, help='The number of values to print')
    parser.add_argument('p', type=int, help='The number of players', default=2, nargs='?')
    args = parser.parse_args()
    if kind == '2':
        kind_str = ''
    else:
        kind_str = f' ({args.p} selected)'
    print(f'The Thue-Morse sequence for {kind} Players{kind_str}, Definition {num:02}, up to {args.n} is: ', end='')
    for x, _ in zip(func(args.p), range(args.n)):
        print(x, "", end='')
    print()