from typing import Iterator

from sympy import symbols

from ..args import run


def gen_inf_prod_approx(x, k_max):
    product_term = 1
    for k in range(k_max):
        product_term *= (1 - x**(2**k))
    return product_term


def p2_d15(_: int = 2) -> Iterator[int]:
    n = 1
    x = symbols('x')
    simple_gf = 1 / (1 - x)
    while True:
        approx_prod = gen_inf_prod_approx(x, n.bit_length() - 1)
        gen_func = (simple_gf - approx_prod) / 2
        series_expansion = gen_func.series(x, 0, n).removeO()  # Remove the Big-O term
        yield from (series_expansion.coeff(x, i) for i in range(n >> 1, n))
        n <<= 1


if __name__ == '__main__':
    run(15, p2_d15, '2')
