from typing import Generator

from sympy import sqrt, symbols

from ..args import run
from ..compat.fluidpythran import boost


@boost
def p2_d18(_: int = 2) -> Generator[int, None, None]:
    n = 8
    nr1 = 0  # normally is n right-shifted 1
    x = symbols('x')
    g_f = (sqrt(x + 1) - sqrt(1 - 3 * x)) / (2 * (x + 1)**(3/2))
    while True:
        series_expansion = g_f.series(x, 0, n + 1)
        for i in range(nr1, n):
            if i > 40:
                raise RuntimeError("sympy runs out of precision past here")
            yield (1 - (-1)**round(series_expansion.coeff(x, i).evalf())) // 2
        nr1 = n
        n <<= 1


if __name__ == '__main__':
    run(18, p2_d18, '2')
