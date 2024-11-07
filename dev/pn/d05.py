from ctypes import c_uint8
from itertools import chain, islice
from typing import Iterator

from ..args import run
from ..p2.d05 import rotate


def pn_d05(n: int = 2) -> Iterator[int]:
    if n < 2 or n > 256:
        raise ValueError("Due to memory use optimizations, this iterator only supports bases 2 thru 256")
    seq = bytearray(range(n))
    prev_len = 0
    while True:
        yield from islice(seq, prev_len, None)
        prev_len = len(seq)
        seq = bytearray(chain.from_iterable(rotate(seq, prev_len // n * i) for i in range(n)))


if __name__ == '__main__':
    run(5, pn_d05, 'N')
