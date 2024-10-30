from itertools import chain, islice
from typing import Iterator, Tuple

from .args import run


def rotate(t: Tuple[int, ...], n: int) -> Tuple[int, ...]:
    return (*t[n:], *t[:n])


def seq_pn_d04(n: int = 2) -> Iterator[int]:
    seq: Tuple[int, ...] = tuple(range(n))
    prev_len = 0
    while True:
        yield from islice(seq, prev_len, None)
        prev_len = len(seq)
        seq += sum((rotate(seq, prev_len // n * i) for i in range(1, n)), start=())


if __name__ == '__main__':
    run(4, seq_pn_d04, 'N')
