from ctypes import c_uint8
from itertools import chain, islice
from typing import Iterator, Tuple

from ..args import run
from ..p2.d04 import rotate
from ..pn.d02 import fill_ctypes_array


def pn_d04(n: int = 2) -> Iterator[int]:
    if n < 2 or n > 255:
        raise ValueError("Due to memory use optimizations, this iterator only supports bases 2 thru 255")
    capacity = n
    seq = (c_uint8 * capacity)()
    fill_ctypes_array(seq, range(n), n)
    prev_len = 0
    while True:
        yield from islice(seq, prev_len, None)
        prev_len = capacity
        capacity *= n
        new_seq = (c_uint8 * capacity)()
        fill_ctypes_array(
            new_seq,
            chain.from_iterable(rotate(seq, prev_len // n * i) for i in range(n)),
            capacity
        )
        seq = new_seq


if __name__ == '__main__':
    run(4, pn_d04, 'N')
