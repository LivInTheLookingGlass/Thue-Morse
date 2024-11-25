from functools import reduce
from operator import mul
from typing import Generator

try:
    from symengine import expand, symbols
except ImportError:
    from sympy import expand, symbols

from ..args import run
from ..compat.fluidpythran import boost


@boost
def p2_d15(_: int = 2) -> Generator[int, None, None]:
    start = 3
    n = 1 << start
    nr1 = 0
    k = start
    x = symbols('x')
    approx_prod = reduce(mul, (1 - x**(1 << i) for i in range(start)))
    while True:
        approx_prod = expand(approx_prod * (1 - x**(1 << k)))
        for i in range(nr1, n):
            yield (1 - int(approx_prod.coeff(x, i))) // 2
        nr1 = n
        n <<= 1
        k += 1


if __name__ == '__main__':
    run(15, p2_d15, '2')
