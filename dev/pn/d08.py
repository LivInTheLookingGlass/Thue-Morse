from itertools import chain, islice
from typing import Iterator

import numpy as np

from ..args import run
from ..compat.fluidpythran import boost
from .d03 import np_select_type


@boost
def pn_d08(n: int = 2) -> Iterator[int]:
    dtype = np_select_type(n)
    seq = np.arange(n, dtype=dtype)
    square = np.array([np.roll(seq, -i) for i in range(n)], dtype=dtype)
    prev_len = 0
    while True:
        yield from islice(seq, prev_len, None)
        prev_len = len(seq)
        seq = np.fromiter(chain.from_iterable(
            square[x] for x in seq
        ), dtype=dtype)


if __name__ == '__main__':
    run(8, pn_d08, 'n')
