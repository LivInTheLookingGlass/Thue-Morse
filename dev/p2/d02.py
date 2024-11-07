from itertools import count
from typing import Iterator

from ..args import run


def p2_d02(_: int = 2) -> Iterator[int]:
    for x in count():
        yield (1 - (-1)**(x.bit_count())) >> 1


if __name__ == '__main__':
    run(1, p2_d02, '2')
