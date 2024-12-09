from itertools import chain
from typing import Generator, Optional, Union

try:
    from z3 import If, Int, IntSort, RecAddDefinition, RecFunction
except ImportError:
    pass

from ..args import run
from ..compat.fluidpythran import boost
from .d11 import odious
from .d12 import evil


@boost
def p2_d14(_: int = 2, size_hint: Optional[int] = None) -> Generator[int, None, None]:
    yield from map(lambda x: 1 - x & 1, chain.from_iterable(zip(odious(), evil())))


def to_z3(_: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    fe = RecFunction('fe2_14', IntSort(), IntSort())
    fo = RecFunction('fo2_14', IntSort(), IntSort())
    p = RecFunction('p2_14', IntSort(), IntSort())
    e = RecFunction('e2_14', IntSort(), IntSort())
    o = RecFunction('o2_14', IntSort(), IntSort())
    T2_14 = RecFunction('T2_14', IntSort(), IntSort())
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
    RecAddDefinition(T2_14, [n], (e(n) + 1) % 2)
    return T2_14


if __name__ == '__main__':
    run(14, p2_d14, '2')
