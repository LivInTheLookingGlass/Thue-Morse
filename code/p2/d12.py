from itertools import count
from typing import Iterator

from ..args import run


def gould(n: int) -> int:
    binomial_coeff = 1
    partial_sum = 0
    for k in range(n + 1):
        # Add the current term to the total sum
        partial_sum += binomial_coeff % 2
        # C(n, k) = C(n, k-1) * (n - (k - 1)) / k
        binomial_coeff = binomial_coeff * (n - k) // (k + 1)
    return partial_sum


def p2_d12(_: int = 2) -> Iterator[int]:
    for i in count():
        yield (gould(i) - 1) % 3


if __name__ == '__main__':
    run(12, p2_d12, '2')
