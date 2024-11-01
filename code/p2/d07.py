from functools import cache
from itertools import count
from math import ceil, floor
from typing import Iterator

from ..args import run


@cache
def b(n: int) -> int:
    if n <= 1:
        return n
    n2 = n / 2
    return b(ceil(n2)) - b(floor(n2))


def p2_d07(_: int = 2) -> Iterator[int]:
    for i in count(1):
        yield (1 - b(2 * i - 1)) // 2


if __name__ == '__main__':
    run(7, p2_d07, '2')
