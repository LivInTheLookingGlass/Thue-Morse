from typing import Generator, Optional, Union

try:
    from z3 import If, Int, IntSort, RecAddDefinition, RecFunction
except ImportError:
    pass

from ..args import run
from ..compat.fluidpythran import boost
from ..compat.int import bit_count
from ..compat.numba import jit


@jit(nopython=True)
def A1510481(n: int, bc: int) -> int:
    n1 = n + 1
    return (n1 >> 1) + ((bc & 1) * (n1 & 1))


@boost
def p2_d13(
    _: int = 2,
    size_hint: Optional[int] = None,
    benchmark: bool = False
) -> Generator[int, None, None]:
    i = -1
    j = jbc = 0
    k = kbc = 1
    while True:
        yield 1 - A1510481(j, kbc) + A1510481(i, jbc)
        i = j
        j = k
        k += 1
        jbc = kbc
        kbc = bit_count(k)


def to_z3(_: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    ilog2 = RecFunction('ilog2_2_13', IntSort(), IntSort())
    p = RecFunction('p2_13', IntSort(), IntSort())
    T2_13 = RecFunction('T2_13', IntSort(), IntSort())
    RecAddDefinition(ilog2, [n], If(n <= 1, 0,
                                    1 + ilog2(n / 2)))
    RecAddDefinition(p, [n], n / 2 + (ilog2(n + 1) % 2) * (n % 2))
    RecAddDefinition(T2_13, [n], 1 - p(n + 1) + p(n))
    return T2_13


if __name__ == '__main__':
    run(13, p2_d13, '2')
