from cmath import exp, pi
from typing import Iterator

from numba import jit

from ..args import run
from .d01 import p


@jit(nopython=False)
def croot(k, n):
    if n <= 0:
        return None
    return exp((2 * pi * 1j * k) / n)


@jit(nopython=False)
def closest_complex(target, complex_list):
    distances = [abs(target - c) for c in complex_list]
    return distances.index(min(distances))


def pn_d02(n: int = 2) -> Iterator[int]:
    roots = [croot(k, n) for k in range(n)]
    x = 0
    while True:
        yield closest_complex(roots[1]**(p(x, n)), roots)
        x += 1


if __name__ == '__main__':
    run(2, pn_d02, 'N')
