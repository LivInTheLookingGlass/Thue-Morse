from itertools import chain, islice
from typing import Generator, Optional, Union

try:
    from z3 import (Concat, If, Int, IntSort, Length, RecAddDefinition, RecFunction, String, StringSort, StringVal,
                    SubString)
except ImportError:
    pass

from ..args import run
from ..compat.bitarray import bitarray
from ..compat.fluidpythran import boost


@boost
def p2_d09(
    _: int = 2,
    size_hint: Optional[int] = None,
    benchmark: bool = False
) -> Generator[int, None, None]:
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
    sub = RecFunction('sub2_09', StringSort(), StringSort(), StringSort())
    t = RecFunction('t2_09', IntSort(), StringSort())
    ilog2 = RecFunction('ilog2_2_09', IntSort(), IntSort())
    T2_09 = RecFunction('T2_09', IntSort(), IntSort())
    RecAddDefinition(sub, [r, s], If(Length(s) == 0, r,
                                     Concat(r, Concat(If(SubString(s, 0, 1) == StringVal("0"),
                                                         StringVal("01"),
                                                         StringVal("10")),
                                                      SubString(s, 1, Length(s) - 1)))))
    RecAddDefinition(t, [n], If(n == 0, StringVal('0'),
                                sub(StringVal(""), t(n - 1))))
    RecAddDefinition(ilog2, [n], If(n <= 1, 0,
                                    1 + ilog2(n / 2)))
    RecAddDefinition(T2_09, [n], If(SubString(t(ilog2(n) + 1), n, 1) == StringVal("0"), 0, 1))
    return T2_09


if __name__ == '__main__':
    run(9, p2_d09, '2')
