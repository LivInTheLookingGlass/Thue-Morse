from itertools import count
from typing import Generator, Optional, Union

try:
    from z3 import If, Int, IntSort, RecAddDefinition, RecFunction
except ImportError:
    pass

from ..args import run
from ..compat.fluidpythran import boost
from ..compat.numba import jit


@jit(nopython=True)
def T(n: int) -> int:
    if n == 0:
        return 0
    return (n - T(n >> 1)) & 1


@boost
def p2_d04(_: int = 2, size_hint: Optional[int] = None) -> Generator[int, None, None]:
    yield from map(T, count())


def to_z3(_: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    p = RecFunction('p2_04', IntSort(), IntSort())
    T2_04 = RecFunction('T2_04', IntSort(), IntSort())
    RecAddDefinition(p, [n], If(n == 0, 0,
                                (n - p(n / 2)) % 2))
    RecAddDefinition(T2_04, [n], p(n))
    return T2_04


if __name__ == '__main__':
    run(4, p2_d04, '2')
