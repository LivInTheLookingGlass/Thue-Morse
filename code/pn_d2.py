from itertools import islice
from typing import Iterator

from .args import run


def seq_pn_d2(n: int = 2) -> Iterator[int]:
    seq = tuple(range(n))
    prev_len = 0
    while True:
        yield from islice(seq, prev_len, None)
        prev_len = len(seq)
        seq += tuple((x + 1) % n for x in seq)


if __name__ == '__main__':
    args = run(2, seq_pn_d2, 'n')
