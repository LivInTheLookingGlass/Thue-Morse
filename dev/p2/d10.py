from itertools import count
from typing import Iterator

from ..args import run


def evil(_: int = 2) -> Iterator[int]:
    for i in count():
        if i.bit_count() & 1 == 0:
            yield i


def p2_d10(_: int = 2) -> Iterator[int]:
    for n, i in enumerate(evil()):
        yield (i - (n << 1)) & 1


if __name__ == '__main__':
    run(10, p2_d10, '2')
