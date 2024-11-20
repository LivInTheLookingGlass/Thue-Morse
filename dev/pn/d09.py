from functools import reduce
from operator import mul
from typing import Iterator

from sympy import I, exp, expand, log, pi, symbols

from ..args import run
from ..compat.fluidpythran import boost


@boost
def pn_d09(s: int = 2) -> Iterator[int]:
    start = 3
    n = s**start
    nts = 0  # usually <previous n> * s, except at first
    k = start
    x = symbols('x')
    i = symbols('i')
    log_omega_s = 2 * pi * I / s
    omega_s = exp(log_omega_s)
    gen_func = reduce(mul, (
        sum(omega_s**i * x**(s**k * i) for i in range(s)) for k in range(start)
    ))
    while True:
        gen_func *= sum(omega_s**i * x**(s**k * i) for i in range(s))
        series_expansion = expand(gen_func.series(x, 0, n).removeO())
        for index in range(nts, n):
            coeff = series_expansion.coeff(x, index)
            if coeff == 0:
                yield 0
                continue
            power = log(coeff) / log_omega_s % s
            if power.is_integer:
                yield int(power)
            else:
                yield round(power.evalf())  # just in case there is floating point drift
        nts = n
        n *= s
        k += 1


if __name__ == '__main__':
    run(9, pn_d09, 'n')
