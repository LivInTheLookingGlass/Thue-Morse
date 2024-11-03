from ctypes import Array
from itertools import islice
from typing import Any, Iterator, Sequence, TypeVar, overload

from bitarray import bitarray

from ..args import run

T = TypeVar("T", Sequence[Any], Array[Any], bitarray)


@overload
def rotate(t: bitarray, n: int) -> bitarray | Sequence[int]:
    ...


@overload
def rotate(t: Array[Any], n: int) -> Array[Any] | Sequence[int]:
    ...


@overload
def rotate(t: Sequence[Any], n: int) -> Sequence[Any]:
    ...


def rotate(t, n):
    return n and (*t[n:], *t[:n]) or t


def p2_d04(_: int = 2) -> Iterator[int]:
    seq: bitarray = bitarray((0, 1))
    prev_len = 0
    while True:
        yield from islice(seq, prev_len, None)
        prev_len = len(seq)
        seq.extend(rotate(seq, prev_len // 2))


if __name__ == '__main__':
    run(4, p2_d04, '2')
