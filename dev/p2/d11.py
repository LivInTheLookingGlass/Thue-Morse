from typing import Iterator, Union

from numba import jit

try:
    from z3 import If, Int, IntSort, RecAddDefinition, RecFunction
except ImportError:
    pass

from ..args import run


@jit(nopython=False)
def A1510481(n: int, bc: int):
    n1 = n + 1
    return (n1 >> 1) + ((bc & 1) * (n1 & 1))


def p2_d11(_: int = 2) -> Iterator[int]:
    i, j, k = (-1, 0, 1)
    while True:
        yield 1 - A1510481(j, k.bit_count()) + A1510481(i, j.bit_count())
        i, j, k = (j, k, k + 1)


def to_z3(_: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    ilog2 = RecFunction('ilog2_2_11', IntSort(), IntSort())
    p = RecFunction('p2_11', IntSort(), IntSort())
    T2_11 = RecFunction('T2_11', IntSort(), IntSort())
    RecAddDefinition(ilog2, [n], If(n <= 1, 0,
                                    1 + ilog2(n / 2)))
    RecAddDefinition(p, [n], n / 2 + (ilog2(n + 1) % 2) * (n % 2))
    RecAddDefinition(T2_11, [n], 1 - p(n + 1) + p(n))
    return T2_11


if __name__ == '__main__':
    run(11, p2_d11, '2')
