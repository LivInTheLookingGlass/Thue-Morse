from itertools import islice
from typing import Iterator

import numpy as np

from ..args import run
from .d03 import np_select_type


def pn_d04(n: int = 2) -> Iterator[int]:
    dtype = np_select_type(n)
    seq = np.arange(n, dtype=dtype)
    prev_len = 0
    while True:
        yield from islice(seq, prev_len, None)
        prev_len = len(seq)
        new_seq = []
        for x in seq:
            new_seq.append(np.arange(x, n, dtype=dtype))
            new_seq.append(np.arange(0, x, dtype=dtype))
        seq = np.concatenate(new_seq)


if __name__ == '__main__':
    run(4, pn_d04, 'n')
