from itertools import count
from typing import Iterator

from numpy.math import comb as binomial

from .args import run


def gould(i: int) -> int:
    partial_sum = 0
    for k in range(i + 1):
        partial_sum += binomial(i, k) % 2
    return partial_sum


def seq_p2_d09(_: int = 2) -> Iterator[int]:
    for i in count():
        yield (gould(i) - 1) % 3


if __name__ == '__main__':
    run(9, seq_p2_d09, '2')
