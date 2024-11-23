from itertools import count
from typing import Iterator, Union

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
def p2_d06(_: int = 2) -> Iterator[int]:
    for i in count():
        yield T(i)


def to_z3(_: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    p = RecFunction('p2_06', IntSort(), IntSort())
    T2_06 = RecFunction('T2_06', IntSort(), IntSort())
    RecAddDefinition(p, [n], If(n == 0, 0,
                                (n - p(n / 2)) % 2))
    RecAddDefinition(T2_06, [n], p(n))
    return T2_06


if __name__ == '__main__':
    run(6, p2_d06, '2')
