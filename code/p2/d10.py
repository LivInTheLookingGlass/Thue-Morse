from itertools import count
from typing import Iterator

from ..args import run


def A1510481(n):
    n1 = n + 1
    return n1 // 2 + ((n1.bit_count() % 2) * (n1 % 2))


def p2_d10(_: int = 2) -> Iterator[int]:
    for i in count():
        yield 1 - A1510481(i) + A1510481(i - 1)


if __name__ == '__main__':
    run(10, p2_d10, '2')
