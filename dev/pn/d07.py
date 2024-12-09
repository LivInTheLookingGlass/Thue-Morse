from itertools import chain, islice
from typing import Generator, Optional, Union

import numpy as np

try:
    from z3 import (Concat, If, Int, IntSort, Length, RecAddDefinition, RecFunction, String, StringSort, StringVal,
                    SubString)
except ImportError:
    pass

from ..args import np_select_type, run
from ..compat.fluidpythran import boost
from ..p2.d10 import rotate


@boost
def pn_d07(
    n: int = 2,
    size_hint: Optional[int] = None,
    benchmark: bool = False
) -> Generator[int, None, None]:
    dtype = np_select_type(n)
    seq = np.arange(n, dtype=dtype)
    prev_len = 0
    while True:
        for i in islice(seq, prev_len, None):
            yield int(i)
        prev_len = len(seq)
        seq = np.fromiter(chain.from_iterable(rotate(seq, prev_len // n * i) for i in range(n)), dtype=dtype)


def to_z3(s: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    r = String('r')
    u = String('u')
    digits = StringVal("0123456789")
    zeros = RecFunction('zerosn_07', IntSort(), StringSort())
    rot = RecFunction('rotn_07', StringSort(), IntSort(), StringSort())
    dig = RecFunction('digitn_07', IntSort(), StringSort())
    undig = RecFunction('undigitn_07', StringSort(), IntSort())
    index = RecFunction('indexn_07', StringSort(), StringSort(), IntSort())
    t = RecFunction('tn_07', IntSort(), StringSort())
    t1 = RecFunction('t1n_07', IntSort(), StringSort())
    ilogn = RecFunction('ilogn_n_07', IntSort(), IntSort())
    ilog10 = RecFunction('ilog10_n_07', IntSort(), IntSort())
    T2_07 = RecFunction('Tn_07', IntSort(), IntSort())
    RecAddDefinition(zeros, [n], If(n == 0, StringVal(""), Concat(StringVal("0"), zeros(n - 1))))
    RecAddDefinition(index, [r, u], If(r == SubString(u, 0, Length(r)), 0,
                                       1 + index(r, SubString(u, Length(r), Length(u) - Length(r)))))
    RecAddDefinition(dig, [n], If(n < 10, Concat(zeros(ilog10(s) - 1), SubString(digits, n % 10, 1)),
                                  Concat(SubString(dig(n / 10), 1, ilog10(s) - 1),
                                         SubString(dig(n % 10), ilog10(s) - 1, 1))))
    RecAddDefinition(undig, [r], If(Length(r) == 1, index(r, digits),
                                    10 * index(SubString(r, 0, 1), digits) + undig(SubString(r, 1, Length(r) - 1))))
    RecAddDefinition(rot, [r, n], Concat(SubString(r, n, Length(r) - n), SubString(r, 0, n)))
    RecAddDefinition(t1, [n], If(n == s, StringVal(""),
                                 Concat(dig(n), t1(n + 1))))
    RecAddDefinition(t, [n], If(n == 0, dig(0),
                                If(n == 1, t1(0),
                                   Concat(t(n - 1), rot(t(n - 1), Length(t(n - 1)) / 2)))))
    RecAddDefinition(ilog10, [n], If(n <= 1, 0,
                                     1 + ilog10(n / 10)))
    RecAddDefinition(ilogn, [n], If(n <= 1, 0,
                                    1 + ilogn(n / s)))
    RecAddDefinition(T2_07, [n], undig(SubString(t(ilogn(n) + 1), n * ilog10(s), ilog10(s))))
    return T2_07


if __name__ == '__main__':
    run(7, pn_d07, 'N')
