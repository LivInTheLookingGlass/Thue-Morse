from itertools import islice
from typing import Iterator, Sequence, TypeVar, overload

from ..args import bitarray, run

T = TypeVar("T")


@overload
def rotate(t: Sequence[T], n: int) -> Sequence[T]:
    ...


@overload
def rotate(t: bitarray, n: int) -> bitarray:
    ...


def rotate(t, n: int):
    return n and (t[n:] + t[:n]) or t


def p2_d05(_: int = 2) -> Iterator[int]:
    seq: bitarray = bitarray((0, 1))
    prev_len = 0
    while True:
        yield from islice(seq, prev_len, None)
        prev_len = len(seq)
        seq.extend(rotate(seq, prev_len >> 1))


if __name__ == '__main__':
    run(5, p2_d05, '2')
