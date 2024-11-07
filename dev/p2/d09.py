from itertools import count
from typing import Iterator

from ..args import run


def odious() -> Iterator[int]:
    for i in count():
        if i.bit_count() & 1:
            yield i


def p2_d09(_: int = 2) -> Iterator[int]:
    for i in odious():
        yield (i + 1) & 1


if __name__ == '__main__':
    run(9, p2_d09, '2')
