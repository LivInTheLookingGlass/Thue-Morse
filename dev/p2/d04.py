from ctypes import Array
from itertools import chain, islice
from typing import Iterator, Sequence, TypeVar, overload

from ..args import bitarray, run
from ..pn.d02 import fill_ctypes_array

T = TypeVar("T")


@overload
def rotate(t: Sequence[T], n: int) -> Sequence[T]:
    ...


@overload
def rotate(t: bitarray, n: int) -> bitarray:
    ...


@overload
def rotate(t: Array, n: int) -> Array:
    ...


def rotate(t, n: int):
    if isinstance(t, Array):
        if not n:
            return t
        new = (t._type_ * len(t))()
        fill_ctypes_array(new, chain(t[n:], t[:n]), len(t))
        return new
    if isinstance(t, bitarray):
        return n and (t[n:] + t[:n]) or t
    if isinstance(t, Sequence):
        return n and (*t[n:], *t[:n]) or t
    raise TypeError("Not a registered type")


def p2_d04(_: int = 2) -> Iterator[int]:
    seq: bitarray = bitarray((0, 1))
    prev_len = 0
    while True:
        yield from islice(seq, prev_len, None)
        prev_len = len(seq)
        seq.extend(rotate(seq, prev_len >> 1))


if __name__ == '__main__':
    run(4, p2_d04, '2')
