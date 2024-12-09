from itertools import count
from typing import Generator, Optional

import numpy as np

from ..args import run
from ..compat.fluidpythran import boost
from ..compat.numba import jit
from .d01 import get_p


@jit(nopython=True)
def closest_root(target: complex, roots: 'np.typing.NDArray[np.complex64]') -> int:
    distances = np.abs(roots - target)  # vectorized
    return int(np.argmin(distances))


@boost
def pn_d02(
    n: int = 2,
    size_hint: Optional[int] = None,
    benchmark: bool = False
) -> Generator[int, None, None]:
    p = get_p(n)
    roots = np.exp(1j * np.linspace(0, 2 * np.pi, abs(n), endpoint=False, dtype=np.complex64))  # vectorized
    primitive_root = roots[1]
    yield from map(lambda x: closest_root(primitive_root**p(x, n), roots), count())


if __name__ == '__main__':
    run(2, pn_d02, 'N')
