from typing import Iterator

from sympy import expand, symbols

from ..args import run


def p2_d15(_: int = 2) -> Iterator[int]:
    n = 1
    nr1 = 0
    k = 1
    x = symbols('x')
    simple_gf = expand(1 / (1 - x))
    approx_prod = 1 - x
    while True:
        approx_prod *= (1 - x**(1 << k))
        gen_func = (simple_gf - approx_prod) / 2
        series_expansion = expand(gen_func.series(x, 0, n).removeO())
        yield from (series_expansion.coeff(x, i) for i in range(nr1, n))
        nr1 = n
        n <<= 1
        k += 1


if __name__ == '__main__':
    run(15, p2_d15, '2')
