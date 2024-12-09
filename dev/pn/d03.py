from functools import partial
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
def T(x: int, n: int) -> int:
    if x == 0:
        return 0
    return (x + T(x // n, n)) % n


@boost
def pn_d03(
    n: int = 2,
    size_hint: Optional[int] = None,
    benchmark: bool = False
) -> Generator[int, None, None]:
    yield from map(partial(T, n=n), count())


def to_z3(s: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    p = RecFunction('pn_03', IntSort(), IntSort())
    Tn_03 = RecFunction('Tn_03', IntSort(), IntSort())
    RecAddDefinition(p, [n], If(n == 0, 0,
                                (n - p(n / s)) % s))
    RecAddDefinition(Tn_03, [n], p(n))
    return Tn_03


if __name__ == '__main__':
    run(3, pn_d03, 'n')
