from itertools import islice
from typing import Iterator, Tuple

from .args import run


def seq_p2_d02(_: int = 2) -> Iterator[int]:
    seq: Tuple[int, ...] = (0, 1)
    prev_len = 0
    while True:
        yield from islice(seq, prev_len, None)
        prev_len = len(seq)
        seq += tuple(0 if x else 1 for x in seq)


if __name__ == '__main__':
    run(2, seq_p2_d02, '2')
