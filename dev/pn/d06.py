from itertools import chain, islice
from typing import Generator, Optional

import numpy as np

from ..args import np_select_type, run
from ..compat.fluidpythran import boost


@boost
def pn_d06(
    n: int = 2,
    size_hint: Optional[int] = None,
    benchmark: bool = False
) -> Generator[int, None, None]:
    dtype = np_select_type(n)
    seq = np.arange(n, dtype=dtype)
    prev_len = 0
    while True:
        for i in islice(seq, prev_len, None):
            yield int(i)
        prev_len = len(seq)
        seq = np.fromiter(chain.from_iterable(
            (*range(x, n), *range(0, x))
            for x in seq
        ), dtype=dtype)


if __name__ == '__main__':
    run(6, pn_d06, 'n')
