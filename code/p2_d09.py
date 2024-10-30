from itertools import count
from typing import Iterator

from .args import run

def A159481(n):
    n1 = n + 1
    return n1 // 2 + ((n1.bit_count() % 2) * (n1 % 2))


def seq_p2_d09(_: int = 2) -> Iterator[int]:
    for i in count():
        yield 1 - A159481(i) + A159481(i - 1)


if __name__ == '__main__':
    run(9, seq_p2_d09, '2')
