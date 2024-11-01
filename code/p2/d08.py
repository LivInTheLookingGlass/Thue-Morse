from itertools import count
from typing import Iterator

from ..args import run


def odious() -> Iterator[int]:
    for i in count():
        if i.bit_count() % 2:
            yield i


def p2_d08(_: int = 2) -> Iterator[int]:
    for i in odious():
        yield (i + 1) % 2


if __name__ == '__main__':
    run(8, p2_d08, '2')
