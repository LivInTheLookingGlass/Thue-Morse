from itertools import chain, islice
from typing import Iterator

import numpy as np

from ..args import run
from ..compat.fluidpythran import boost


@boost
def np_select_type(n: int) -> np.typing.DTypeLike:
    if n < 2:
        raise ValueError("Doesn't support unary or negative bases")
    if n < (1 << 7):
        return np.uint8
    if n < (1 << 15):
        return np.uint16
    if n < (1 << 31):
        return np.uint32
    if n < (1 << 63):
        return np.uint64
    try:
        if n < (1 << 127):
            return np.uint128
    except AttributeError:  # np.uint128 and higher is conditionally supported
        raise ValueError(f"Your base is too large to support efficiently (max is {(1 << 63) - 1})")
    try:
        if n < (1 << 255):
            return np.uint256
    except AttributeError:  # np.uint256 is conditionally supported
        raise ValueError(f"Your base is too large to support efficiently (max is {(1 << 127) - 1})")
    raise ValueError(f"Your base is too large to support efficiently (max is {(1 << 255) - 1})")


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
