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
def xor_in_n(a, b, n):
    if a < 1:
        return b
    if b < 1:
        return a
    res = 0
    ni = 1
    while a > 0 or b > 0:
        a_digit = a % n
        b_digit = b % n
        res += ((a_digit - b_digit) % n) * ni
        a //= n
        b //= n
        ni *= n
    return res


@jit(nopython=True)
def xor_wrapper(x: int, n: int, value: int) -> int:
    xored = xor_in_n(x, (x - 1), n)
    lx = -1
    while xored:  # manually implement log
        lx += 1
        xored //= n
    return (lx + value + 1) % n


@boost
def pn_d04(
    n: int = 2,
    size_hint: Optional[int] = None,
    benchmark: bool = False
) -> Generator[int, None, None]:
    yield from (0, 1)
    value = 1
    for x in count(2):
        value = xor_wrapper(x, n, value)
        yield value


def to_z3(s: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    x = Int('x')
    y = Int('y')
    ilogn = RecFunction('ilog2n_04', IntSort(), IntSort(), IntSort())
    xorn = RecFunction('xornn_04', IntSort(), IntSort(), IntSort(), IntSort())
    p = RecFunction('pn_04', IntSort(), IntSort())
    Tn_04 = RecFunction('Tn_04', IntSort(), IntSort())
    RecAddDefinition(xorn, [x, y, n],
                     If(x == 0, y,
                        If(y == 0, x,
                           ((x % n) + (y % n)) % n + n * xorn(x / n, y / n, n))))
    RecAddDefinition(ilogn, [x, y],
                     If(x <= 1, 0,
                        1 + ilogn(x / y, y)))
    RecAddDefinition(p, [n], ilogn(xorn(n, (n - 1), s), s) + 1)
    RecAddDefinition(Tn_04, [n],
                     If(n < s, n,
                        (ilogn(xorn(n, n - 1, s), s) + Tn_04(n - 1) + 1) % s))
    return Tn_04


if __name__ == '__main__':
    run(4, pn_d04, 'N')
