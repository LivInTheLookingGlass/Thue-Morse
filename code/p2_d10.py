from functools import reduce
from itertools import count
from operator import xor
from typing import Iterator

from numpy.math import comb as binomial

from .args import run


def A001317(n: int) -> int:
    return sum((binomial(n, k) % 2) * 2**k for k in range(n + 1))


def seq_p2_d10(_: int = 2) -> Iterator[int]:
    for i in count():
        yield reduce(
            xor,
            (A001317(idx) for idx, value in enumerate(bin(i)[2:]) if value == '1'),
            0
        ) % 2


if __name__ == '__main__':
    run(10, seq_p2_d10, '2')
