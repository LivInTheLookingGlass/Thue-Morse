from itertools import count
from math import comb as binomial
from typing import Iterator

from .args import run


def gould(i: int) -> int:
    partial_sum = 0
    for k in range(i + 1):
        partial_sum += binomial(i, k) % 2
    return partial_sum


def seq_p2_d11(_: int = 2) -> Iterator[int]:
    for i in count():
        yield (gould(i) - 1) % 3


if __name__ == '__main__':
    run(11, seq_p2_d11, '2')
