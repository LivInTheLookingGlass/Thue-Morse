from itertools import count
from typing import Iterator

from .args import run


def evil(_: int = 2) -> Iterator[int]:
    for i in count():
        if i.bit_count() % 2 == 0:
            yield i


def seq_p2_d09(_: int = 2) -> Iterator[int]:
    for i in evil():
        yield (i - 2 * i) % 2


if __name__ == '__main__':
    run(9, seq_p2_d09, '2')
