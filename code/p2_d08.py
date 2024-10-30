from itertools import count
from typing import Iterator

from .args import run


def seq_p2_d08(_: int = 2) -> Iterator[int]:
    for n, i in enumerate(count()):
        if i.bit_count() % 2 == 0:
            yield (i - 2 * n) % 2


if __name__ == '__main__':
    run(8, seq_p2_d08, '2')
