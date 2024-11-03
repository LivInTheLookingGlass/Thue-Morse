from ctypes import c_uint8
from itertools import islice
from typing import Iterator

from ..args import run


def pn_d02(n: int = 2) -> Iterator[int]:
    seq = tuple((c_uint8(x) for x in range(n)))
    prev_len = 0
    while True:
        yield from map(lambda x: x.value, islice(seq, prev_len, None))
        prev_len = len(seq)
        seq += tuple(c_uint8((x.value + i) % n) for i in range(1, n) for x in seq)


if __name__ == '__main__':
    run(2, pn_d02, 'n')
