from itertools import count
from typing import Generator, Union

try:
    from z3 import If, Int, IntSort, RecAddDefinition, RecFunction, ToInt
except ImportError:
    pass

from ..args import run
from ..compat.fluidpythran import boost
from ..compat.int import bit_count
from ..compat.numba import jit


@jit(nopython=True)
def compute(bc: int) -> int:
    return (1 - (-1)**bc) >> 1


@boost
def p2_d02(_: int = 2) -> Generator[int, None, None]:
    yield from map(lambda x: compute(bit_count(x)), count())


def to_z3(_: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    p = RecFunction('p2_02', IntSort(), IntSort())
    T2_02 = RecFunction('T2_02', IntSort(), IntSort())
    RecAddDefinition(p, [n], If(n == 0, 0,
                                p(n / 2) + (n % 2)))
    RecAddDefinition(T2_02, [n], ToInt((1 - (-1)**p(n)) / 2))
    return T2_02


if __name__ == '__main__':
    run(1, p2_d02, '2')
