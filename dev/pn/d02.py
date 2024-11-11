from cmath import exp, pi
from itertools import count
from typing import Iterator

from ..args import run
from .d01 import p


def croot(k, n):
    if n <= 0:
        return None
    return exp((2 * pi * 1j * k) / n)


def closest_complex(target, complex_list):
    distances = [abs(target - c) for c in complex_list]
    return distances.index(min(distances))


def pn_d02(n: int = 2) -> Iterator[int]:
    roots = [croot(k, n) for k in range(n)]
    for x in count():
        yield closest_complex(roots[1]**(p(x, n)), roots)


if __name__ == '__main__':
    run(2, pn_d02, 'N')
