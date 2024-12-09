from itertools import chain, islice
from typing import Generator, Optional

import numpy as np

from ..args import np_select_type, run
from ..compat.fluidpythran import boost


@boost
def pn_d08(n: int = 2, size_hint: Optional[int] = None) -> Generator[int, None, None]:
    dtype = np_select_type(n)
    seq = np.arange(n, dtype=dtype)
    square = np.array([np.roll(seq, -i) for i in range(n)], dtype=dtype)
    prev_len = 0
    while True:
        for i in islice(seq, prev_len, None):
            yield int(i)
        prev_len = len(seq)
        seq = np.fromiter(chain.from_iterable(
            square[x] for x in seq
        ), dtype=dtype)


if __name__ == '__main__':
    run(8, pn_d08, 'n')
