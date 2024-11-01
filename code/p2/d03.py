from itertools import chain, islice
from typing import Iterator, Tuple

from ..args import run


def p2_d03(_: int = 2) -> Iterator[int]:
    seq: Tuple[int, ...] = (0, )
    prev_len = 0
    while True:
        yield from islice(seq, prev_len, None)
        prev_len = len(seq)
        seq = tuple(chain.from_iterable(
            (0, 1) if x == 0 else (1, 0)
            for x in seq
        ))


if __name__ == '__main__':
    run(3, p2_d03, '2')
