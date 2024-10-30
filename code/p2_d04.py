from itertools import chain, islice
from typing import Iterator, Tuple

from .args import run


def rotate(t: Tuple[int, ...], n: int) -> Tuple[int, ...]:
    return (*t[n:], *t[:n])


def seq_p2_d04(_: int = 2) -> Iterator[int]:
    seq: Tuple[int, ...] = (0, 1)
    prev_len = 0
    while True:
        yield from islice(seq, prev_len, None)
        prev_len = len(seq)
        seq += rotate(seq, prev_len // 2)


if __name__ == '__main__':
    run(4, seq_p2_d04, '2')
