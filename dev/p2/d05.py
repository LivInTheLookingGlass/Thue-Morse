from itertools import islice
from typing import Iterator, Sequence, TypeVar, Union, overload

try:
    from z3 import (Concat, If, Int, IntSort, Length, RecAddDefinition, RecFunction, String, StringSort, StringVal,
                    SubString)
except ImportError:
    pass

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


def to_z3(_: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    s = String('s')
    rot = RecFunction('rot2_05', StringSort(), IntSort(), StringSort())
    t = RecFunction('t2_05', IntSort(), StringSort())
    ilog2 = RecFunction('ilog2_2_05', IntSort(), IntSort())
    T2_05 = RecFunction('T2_05', IntSort(), IntSort())
    RecAddDefinition(rot, [s, n], Concat(SubString(s, n, Length(s) - n), SubString(s, 0, n)))
    RecAddDefinition(t, [n], If(n == 0, StringVal('0'),
                                If(n == 1, StringVal('01'),
                                   Concat(t(n - 1), rot(t(n - 1), Length(t(n - 1)) / 2)))))
    RecAddDefinition(ilog2, [n], If(n <= 1, 0,
                                    1 + ilog2(n / 2)))
    RecAddDefinition(T2_05, [n], If(SubString(t(ilog2(n) + 1), n, 1) == StringVal("0"), 0, 1))
    return T2_05


if __name__ == '__main__':
    run(5, p2_d05, '2')
