from itertools import count
from operator import mul
from typing import Generator, Optional

from gmpy2 import mpq as Fraction
import numpy as np

from ..args import run
from ..compat.fluidpythran import boost


@boost
def p2_d21(
    _: int = 2,
    size_hint: Optional[int] = None,
    benchmark: bool = False
) -> Generator[int, None, None]:
    q = 1 - Fraction(1, 1 << 128)
    remaining_prob = Fraction(1)
    f = 0
    for x in count():
        value = remaining_prob * q
        if f >= 0:
            yield 0
            f -= value
        else:
            yield 1
            f += value
        remaining_prob *= q


if __name__ == '__main__':
    run(21, p2_d21, '2')
