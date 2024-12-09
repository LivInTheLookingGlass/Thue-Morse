from csv import reader
from pathlib import Path
from typing import Generator, Optional

from sympy import factorial, gamma, hyper, pi, sqrt, symbols

from ..args import run
from ..compat.fluidpythran import boost


def hypergeometric2F1_reg(a, b, c, z):
    return hyper([a, b], [c], z) / gamma(c)


@boost
def p2_d19(
    _: int = 2,
    size_hint: Optional[int] = None,
    benchmark: bool = False
) -> Generator[int, None, None]:
    last_x = 41
    n = symbols('n')
    f = (-1)**n / 2 + (-3)**n * sqrt(pi) * hypergeometric2F1_reg(3 / 2, -n, 3 / 2 - n, -1 / 3) / (4 * factorial(n))
    for x in range(last_x):
        yield (1 + round(f.subs(n, x).evalf(x))) % 2

    if not benchmark:
        # below is a CSV reader which reads output from the following Mathematica code:
        # k1 := 12
        # CloudExport[1 - Mod[Table[(-1)^n/2 + (-3)^n Sqrt[Pi] *
        # Hypergeometric2F1Regularized[3/2, - n, 3/2 - n, - 1/3]/(4 n!), {n, 0, 2^k1 - 1}], 2], "csv"]
        with Path(__file__).parent.joinpath('d19.csv').open(mode='r') as file:
            table = reader(file)

            for _ in range(last_x):
                next(table)

            for row in table:
                yield int(row[0])

    raise RuntimeError("Ran out of terms from Mathematica code-gen (up to 2^12 on free license)")


if __name__ == '__main__':
    run(19, p2_d19, '2')
