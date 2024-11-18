from itertools import count
from typing import Iterator

import numpy as np

from ..args import run
from ..compat.numba import jit
from .d01 import p


@jit
def closest_root(target: complex, roots: np.typing.NDArray[complex]) -> int:
    distances = np.abs(roots - target)  # vectorized
    return np.argmin(distances)


def pn_d02(n: int = 2) -> Iterator[int]:
    roots = np.exp(1j * np.linspace(0, 2 * np.pi, n, endpoint=False))  # vectorized
    primitive_root = roots[1]
    for x in count():
        yield closest_root(primitive_root**p(x, n), roots)


if __name__ == '__main__':
    run(2, pn_d02, 'N')
