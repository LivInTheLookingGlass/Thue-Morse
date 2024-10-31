from itertools import chain, islice
from typing import Iterator, Tuple

from .args import run
from p2_d04 import rotate


def seq_pn_d04(n: int = 2) -> Iterator[int]:
    seq: Tuple[int, ...] = tuple(range(n))
    prev_len = 0
    while True:
        yield from islice(seq, prev_len, None)
        prev_len = len(seq)
        seq = (*chain.from_iterable(rotate(seq, prev_len // n * i) for i in range(n)), )


if __name__ == '__main__':
    run(4, seq_pn_d04, 'N')
