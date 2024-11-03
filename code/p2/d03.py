from itertools import chain, islice
from typing import Iterator

from bitarray import bitarray

from ..args import run


def p2_d03(_: int = 2) -> Iterator[int]:
    seq = bitarray((0, 1))
    prev_len = 0
    while True:
        yield from islice(seq, prev_len, None)
        prev_len = len(seq)
        seq = bitarray(chain.from_iterable((1, 0) if x else (0, 1) for x in seq))


if __name__ == '__main__':
    run(3, p2_d03, '2')
