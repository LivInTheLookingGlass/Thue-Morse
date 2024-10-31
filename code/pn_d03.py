from itertools import chain, islice
from typing import Iterator

from .args import run


def seq_pn_d03(n: int = 2) -> Iterator[int]:
    seq = (0, )
    prev_len = 0
    while True:
        yield from islice(seq, prev_len, None)
        prev_len = len(seq)
        seq = (*chain.from_iterable(
            (*range(x, n), *range(0, x))
            for x in seq
        ), )


if __name__ == '__main__':
    run(3, seq_pn_d03, 'n')
