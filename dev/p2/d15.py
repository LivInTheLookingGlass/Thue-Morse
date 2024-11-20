from functools import reduce
from operator import mul
from typing import Iterator

from sympy import expand, symbols

from ..args import run
from ..compat.fluidpythran import boost


@boost
def p2_d15(_: int = 2) -> Iterator[int]:
    start = 3
    n = 1 << start
    nr1 = 0
    k = start
    x = symbols('x')
    simple_gf = expand(1 / (1 - x))
    approx_prod = reduce(mul, (1 - x**(1 << i) for i in range(start)))
    while True:
        approx_prod *= (1 - x**(1 << k))
        gen_func = (simple_gf - approx_prod) / 2
        series_expansion = expand(gen_func.series(x, 0, n).removeO())
        yield from (int(series_expansion.coeff(x, i)) for i in range(nr1, n))
        nr1 = n
        n <<= 1
        k += 1


if __name__ == '__main__':
    run(15, p2_d15, '2')
