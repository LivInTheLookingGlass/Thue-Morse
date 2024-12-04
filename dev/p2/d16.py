from itertools import count
from typing import Generator

from ..args import run
from ..compat.fluidpythran import boost
from ..compat.numba import jit


@jit(nopython=True)
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


@jit(nopython=True)
def A193231(i: int) -> int:
    ret = 0
    idx = 0
    while i:
        if i & 1:
            ret ^= A001317(idx)
        i >>= 1
        idx += 1
    return ret & 1


@boost
def p2_d16(_: int = 2) -> Generator[int, None, None]:
    yield from map(A193231, count())


if __name__ == '__main__':
    run(16, p2_d16, '2')
