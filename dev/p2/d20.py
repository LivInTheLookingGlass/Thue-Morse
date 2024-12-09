from csv import reader
from pathlib import Path
from typing import Generator, Optional

from ..args import run
from ..compat.fluidpythran import boost


@boost
def p2_d20(
    _: int = 2,
    size_hint: Optional[int] = None,
    benchmark: bool = False
) -> Generator[int, None, None]:
    if not benchmark:
        # below is a CSV reader which reads output from the following Mathematica code:
        # k2 := 15
        # CloudExport[1 - Flatten[CellularAutomaton[{69540422, 2, 2}, {{1}, 0}, 2^k2 - 1, {All, 0}]], "csv"]
        with Path(__file__).parent.joinpath('d20.csv').open(mode='r') as file:
            table = reader(file)
            for row in table:
                yield int(row[0])

    raise RuntimeError("Ran out of terms from Mathematica code-gen (up to 2^15 on free license)")


if __name__ == '__main__':
    run(20, p2_d20, '2')
