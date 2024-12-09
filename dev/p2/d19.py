from typing import Generator, Optional

from sympy import factorial, gamma, hyper, pi, sqrt, symbols

from ..args import run
from ..compat.fluidpythran import boost


def hypergeometric2F1_reg(a, b, c, z):
    return hyper([a, b], [c], z) / gamma(c)


@boost
def p2_d19(_: int = 2, size_hint: Optional[int] = None) -> Generator[int, None, None]:
    n = symbols('n')
    f = (-1)**n / 2 + (-3)**n * sqrt(pi) * hypergeometric2F1_reg(3 / 2, -n, 3 / 2 - n, -1 / 3) / (4 * factorial(n))
    for x in range(41):
        yield (1 + round(f.subs(n, x).evalf(x))) % 2
    raise RuntimeError("sympy runs out of precision past this point")


if __name__ == '__main__':
    run(19, p2_d19, '2')
