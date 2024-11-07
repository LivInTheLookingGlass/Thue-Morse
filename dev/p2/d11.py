from itertools import count
from typing import Iterator

from ..args import run


def A1510481(n):
    n1 = n + 1
    return (n1 >> 1) + ((n1.bit_count() & 1) * (n1 & 1))


def p2_d11(_: int = 2) -> Iterator[int]:
    for i in count():
        yield 1 - A1510481(i) + A1510481(i - 1)


if __name__ == '__main__':
    run(11, p2_d11, '2')
