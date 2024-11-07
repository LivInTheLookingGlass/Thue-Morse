from functools import reduce
from itertools import count
from operator import xor
from typing import Iterator

from ..args import run


def A001317(n: int) -> int:
    exp_2_k = 1
    binomial_coeff = 1
    partial_sum = 0
    for k in range(n + 1):
        # Add the current term to the total sum
        partial_sum += (binomial_coeff & 1) * exp_2_k
        # C(n, k) = C(n, k-1) * (n - (k - 1)) / k
        binomial_coeff = binomial_coeff * (n - k) // (k + 1)
        exp_2_k >>= 1
    return partial_sum


def p2_d14(_: int = 2) -> Iterator[int]:
    for i in count():
        yield reduce(
            xor,
            (A001317(idx) for idx, value in enumerate(bin(i)[2:]) if value == '1'),
            0
        ) & 1


if __name__ == '__main__':
    run(14, p2_d14, '2')
