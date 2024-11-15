from typing import Iterator, Union

from numba import jit

try:
    from z3 import If, Int, IntSort, RecAddDefinition, RecFunction
except ImportError:
    pass

from ..args import run


@jit(nopython=False)
def T(x: int, n: int) -> int:
    if x == 0:
        return 0
    return (x + T(x // n, n)) % n


def pn_d06(n: int = 2) -> Iterator[int]:
    i = 0
    while True:
        yield T(i, n)
        i += 1


def to_z3(s: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    p = RecFunction('pn_06', IntSort(), IntSort())
    Tn_06 = RecFunction('Tn_06', IntSort(), IntSort())
    RecAddDefinition(p, [n], If(n == 0, 0,
                                (n - p(n / s)) % s))
    RecAddDefinition(Tn_06, [n], p(n))
    return Tn_06


if __name__ == '__main__':
    run(6, pn_d06, 'n')
