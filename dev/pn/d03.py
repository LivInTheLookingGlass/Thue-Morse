from itertools import chain, islice
from typing import Iterator

import numpy as np

from ..args import np_select_type, run
from ..compat.fluidpythran import boost


@boost
def pn_d03(n: int = 2) -> Iterator[int]:
    dtype = np_select_type(n)
    seq = np.arange(n, dtype=dtype)
    yield from seq
    prev_len = len(seq)
    while True:
        seq = np.concatenate([seq, np.fromiter(chain.from_iterable((seq + i) % n for i in range(1, n)), dtype=dtype)])
        yield from islice(seq, prev_len, None)
        prev_len = len(seq)


if __name__ == '__main__':
    run(3, pn_d03, 'n')
