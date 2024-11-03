from itertools import chain, islice
from typing import Iterator, Tuple

from ..args import run


def pn_d03(n: int = 2) -> Iterator[int]:
    seq: Tuple[range, ...] = (range(n), )
    prev_len = 1
    yield from range(n)
    while True:
        prev_len *= n
        seq = (*chain.from_iterable(
            (range(x, n), range(0, x))
            for x in chain.from_iterable(seq)
        ), )
        yield from islice(chain.from_iterable(seq), prev_len, None)


if __name__ == '__main__':
    run(3, pn_d03, 'n')
