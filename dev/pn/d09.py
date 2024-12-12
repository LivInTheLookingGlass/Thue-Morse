from functools import reduce
from operator import mul
from typing import Generator, Optional

try:
    from symengine import I, exp, expand, log, pi, symbols
except ImportError:
    from sympy import I, exp, expand, log, pi, symbols

from ..args import run
from ..compat.fluidpythran import boost


@boost
def pn_d09(
    s: int = 2,
    size_hint: Optional[int] = None,
    benchmark: bool = False
) -> Generator[int, None, None]:
    start = 2
    n = s**start
    nts = 0  # usually <previous n> * s, except at first
    k = start
    x = symbols('x')
    log_omega_s = 2 * pi * I / s
    omega_s = exp(log_omega_s)
    gen_func = reduce(mul, (
        sum(omega_s**i * x**(s**k * i) for i in range(s)) for k in range(start)
    ))
    while True:
        gen_func = expand(gen_func * sum(omega_s**i * x**(s**k * i) for i in range(s)))
        for index in range(nts, n):
            coeff = gen_func.coeff(x, index)
            if coeff == 0:
                yield 0
                continue
            power, _ = ((log(coeff) / log_omega_s) % s).evalf().as_real_imag()
            yield round(float(power.evalf())) % s  # just in case there is floating point drift
        nts = n
        n *= s
        k += 1


if __name__ == '__main__':
    run(9, pn_d09, 'n')
