from itertools import count
from typing import Iterator

from .args import run


def seq_p2_d06(_: int = 2) -> Iterator[int]:
    for i in count():
        if bin(i).count('1') % 2:
            yield (i + 1) % 2


if __name__ == '__main__':
    args = run(6, seq_p2_d06, '2')
