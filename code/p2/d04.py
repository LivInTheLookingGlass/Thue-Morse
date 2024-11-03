from itertools import islice
from typing import Iterator, Sequence, TypeVar

from bitarray import bitarray

from ..args import run

T = TypeVar("T")


def rotate(t: Sequence[T], n: int) -> Sequence[T]:
    return n and (*t[n:], *t[:n]) or t


def p2_d04(_: int = 2) -> Iterator[int]:
    seq: bitarray = (0, 1)
    prev_len = 0
    while True:
        yield from islice(seq, prev_len, None)
        prev_len = len(seq)
        seq += rotate(seq, prev_len // 2)


if __name__ == '__main__':
    run(4, p2_d04, '2')
