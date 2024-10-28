from functools import reduce
from itertools import count
from operator import floordiv, mul
from typing import Iterator

from .args import run


def binomial(i: int, k: int) -> int:
    return reduce(
        floordiv,
        range(2, i - k + 1),
        reduce(mul, range(k + 1, i + 1), 1)
    )


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
