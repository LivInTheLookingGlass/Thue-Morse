from csv import reader
from pathlib import Path
from typing import Generator, Optional

from sympy import sqrt, symbols

from ..args import run
from ..compat.fluidpythran import boost


@boost
def p2_d18(
    _: int = 2,
    size_hint: Optional[int] = None,
    benchmark: bool = False
) -> Generator[int, None, None]:
    n = 8
    nr1 = 0  # normally is n right-shifted 1
    broken = False
    last_i = 40
    x = symbols('x')
    g_f = (sqrt(x + 1) - sqrt(1 - 3 * x)) / (2 * (x + 1)**(3 / 2))
    while not broken:
        series_expansion = g_f.series(x, 0, n + 1)
        for i in range(nr1, n):
            if i > last_i:
                broken = True
                break
            yield (1 - (-1)**round(series_expansion.coeff(x, i).evalf())) // 2
        nr1 = n
        n <<= 1

    if not benchmark:
        # below is a CSV reader which reads output from the following Mathematica code:
        # k0 := 11
        # G[x_] := (Sqrt[x + 1] - Sqrt[1 - 3 x])/(2 (x + 1)^(3/2));
        # seriesG = Series[G[x], {x, 0, 2^k0-1}];
        # coefficients = Table[Coefficient[seriesG, x, n], {n, 0, 2^k0-1}];
        # T2[n_] := (1 - (-1)^coefficients[[n + 1]])/2;
        # CloudExport[Table[T2[n], {n, 0, 2^k0-1}], "csv"]
        with Path(__file__).parent.joinpath('d18.csv').open(mode='r') as file:
            table = reader(file)

            for _ in range(last_i):
                next(table)

            for row in table:
                yield int(row[0])

    raise RuntimeError("Ran out of terms from Mathematica code-gen (up to 2^11 on free license)")


if __name__ == '__main__':
    run(18, p2_d18, '2')
