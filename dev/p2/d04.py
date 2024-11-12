from itertools import chain, islice
from typing import Iterator, Union

try:
    from z3 import (Concat, If, Int, IntSort, Length, RecAddDefinition, RecFunction, String, StringSort, StringVal,
                    SubString)
except ImportError:
    pass

from ..args import bitarray, run


def p2_d04(_: int = 2) -> Iterator[int]:
    seq = bitarray((0, 1))
    prev_len = 0
    while True:
        yield from islice(seq, prev_len, None)
        prev_len = len(seq)
        seq = bitarray(chain.from_iterable((1, 0) if x else (0, 1) for x in seq))


def to_z3(_: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    s = String('s')
    r = String('r')
    sub = RecFunction('sub2_04', StringSort(), StringSort(), StringSort())
    t = RecFunction('t2_04', IntSort(), StringSort())
    ilog2 = RecFunction('ilog2_2_04', IntSort(), IntSort())
    T2_04 = RecFunction('T2_04', IntSort(), IntSort())
    RecAddDefinition(sub, [r, s], If(Length(s) == 0, r,
                                     Concat(r, Concat(If(SubString(s, 0, 1) == StringVal("0"),
                                                         StringVal("01"),
                                                         StringVal("10")),
                                                      SubString(s, 1, Length(s) - 1)))))
    RecAddDefinition(t, [n], If(n == 0, StringVal('0'),
                                sub(StringVal(""), t(n - 1))))
    RecAddDefinition(ilog2, [n], If(n <= 1, 0,
                                    1 + ilog2(n / 2)))
    RecAddDefinition(T2_04, [n], If(SubString(t(ilog2(n) + 1), n, 1) == StringVal("0"), 0, 1))
    return T2_04


if __name__ == '__main__':
    run(4, p2_d04, '2')
