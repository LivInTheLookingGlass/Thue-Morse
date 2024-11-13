from itertools import count
from math import log
from typing import Iterator, Union

try:
    from z3 import If, Int, IntSort, RecAddDefinition, RecFunction
except ImportError:
    pass

from ..args import run


def xor_in_n(a, b, n):
    if min(a, b) < 1:
        return max(a, b)
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


def pn_d07(n: int = 2) -> Iterator[int]:
    yield from (0, 1)
    value = 1
    for x in count(2):
        value = int(log(xor_in_n(x, (x - 1), n), n) + value + 1) % n
        yield value


def to_z3(s: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    x = Int('x')
    y = Int('y')
    ilogn = RecFunction('ilog2n_07', IntSort(), IntSort(), IntSort())
    xorn = RecFunction('xornn_07', IntSort(), IntSort(), IntSort(), IntSort())
    p = RecFunction('pn_07', IntSort(), IntSort())
    Tn_07 = RecFunction('Tn_07', IntSort(), IntSort())
    RecAddDefinition(xorn, [x, y, n],
                     If(x == 0, y,
                        If(y == 0, x,
                           ((x % n) + (y % n)) % n + n * xorn(x / n, y / n, n))))
    RecAddDefinition(ilogn, [x, y],
                     If(x <= 1, 0,
                        1 + ilogn(x / y, y)))
    RecAddDefinition(p, [n], ilogn(xorn(n, (n - 1), s), s) + 1)
    RecAddDefinition(Tn_07, [n],
                     If(n < s, n,
                        (ilogn(xorn(n, n - 1, s), s) + Tn_07(n - 1) + 1) % s))
    return Tn_07


if __name__ == '__main__':
    run(7, pn_d07, 'N')
