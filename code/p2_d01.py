from itertools import count
from typing import Iterator

from .args import run


def seq_p2_d01(_: int = 2) -> Iterator[int]:
    for x in count():
        yield x.bit_count() % 2


if __name__ == '__main__':
    run(1, seq_p2_d01, '2')
