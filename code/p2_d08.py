from itertools import count
from typing import Iterator

from .args import run


def seq_p2_d08(_: int = 2) -> Iterator[int]:
    for i in count():
        if i.bit_count() % 2:
            yield (i + 1) % 2


if __name__ == '__main__':
    run(8, seq_p2_d08, '2')
