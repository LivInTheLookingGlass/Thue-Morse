from itertools import tee
from typing import Iterator, Tuple

from ..args import run


def p2_d12(_: int = 2) -> Iterator[int]:
    row: Tuple[int, ...] = (1, )
    while True:
        yield (sum(x % 2 for x in row) - 1) % 3
        it1, it2 = tee(iter(row), 2)
        next(it2)
        row = (1, *(x + y for x, y in zip(it1, it2)), 1)


if __name__ == '__main__':
    run(12, p2_d12, '2')
