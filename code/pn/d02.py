from ctypes import Array, c_uint8, sizeof
from itertools import islice
from typing import Iterable, Iterator

from ..args import run


def fill_ctypes_array(c_array: Array,iterable: Iterable[int], length: int, offset: int) -> None:
    for value, i in zip(iterable, range(length)):
        c_array[offset + i] = c_uint8(value)


def pn_d02(n: int = 2) -> Iterator[int]:
    capacity = n
    seq = (c_uint8 * capacity)()
    fill_ctypes_array(seq, range(n), n, 0)
    prev_len = 0
    while True:
        yield from map(lambda x: x, islice(seq, prev_len, None))
        prev_len = len(seq)
        capacity *= n
        new_seq = (c_uint8 * capacity)()
        fill_ctypes_array(new_seq, seq, prev_len, 0)
        fill_ctypes_array(
            new_seq,
            ((x + i) % n for i in range(1, n) for x in seq),
            prev_len * (n - 1),
            prev_len
        )
        seq = new_seq


if __name__ == '__main__':
    run(2, pn_d02, 'n')
