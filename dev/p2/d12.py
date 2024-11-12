from itertools import chain
from typing import Iterator, Union

try:
    from z3 import If, Int, IntSort, RecAddDefinition, RecFunction
except ImportError:
    pass

from ..args import run
from .d09 import odious
from .d10 import evil


def p2_d12(_: int = 2) -> Iterator[int]:
    for i in chain.from_iterable(zip(odious(), evil())):
        yield 1 - i & 1


def to_z3(_: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    fe = RecFunction('fe2_12', IntSort(), IntSort())
    fo = RecFunction('fo2_12', IntSort(), IntSort())
    p = RecFunction('p2_12', IntSort(), IntSort())
    e = RecFunction('e2_12', IntSort(), IntSort())
    o = RecFunction('o2_12', IntSort(), IntSort())
    T2_12 = RecFunction('T2_12', IntSort(), IntSort())
    RecAddDefinition(p, [n], If(n == 0, 0,
                                p(n / 2) + n))
    RecAddDefinition(fe, [n], If(p(n) % 2 == 0, n,
                                 fe(n + 1)))
    RecAddDefinition(fo, [n], If(p(n) % 2 == 1, n,
                                 fo(n + 1)))
    RecAddDefinition(e, [n], If(n == 0, 0,
                                fe(e(n - 1) + 1)))
    RecAddDefinition(o, [n], If(n == 0, 1,
                                fo(o(n - 1) + 1)))
    RecAddDefinition(T2_12, [n], (e(n) + 1) % 2)
    return T2_12


if __name__ == '__main__':
    run(12, p2_d12, '2')
