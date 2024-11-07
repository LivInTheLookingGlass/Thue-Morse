from itertools import count
from typing import Iterator

from ..args import run


def T(n: int) -> int:
    if n == 0:
        return 0
    return (n - T(n >> 1)) & 1


def p2_d06(_: int = 2) -> Iterator[int]:
    for i in count():
        yield T(i)


if __name__ == '__main__':
    run(6, p2_d06, '2')
