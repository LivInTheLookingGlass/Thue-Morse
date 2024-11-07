from itertools import chain, islice
from typing import Iterator

from ..args import run


def pn_d04(n: int = 2) -> Iterator[int]:
    if n < 2 or n > 256:
        raise ValueError("Due to memory use optimizations, this iterator only supports bases 2 thru 256")
    seq = bytearray(range(n))
    prev_len = 0
    while True:
        yield from islice(seq, prev_len, None)
        prev_len = len(seq)
        seq = bytearray(chain.from_iterable((*range(x, n), *range(0, x)) for x in seq))


if __name__ == '__main__':
    run(4, pn_d04, 'n')
