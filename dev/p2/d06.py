from itertools import count
from typing import Iterator

from ..args import run


def p2_d06(_: int = 2) -> Iterator[int]:
    value = 1
    for n in count():
        # Note: assumes that (-1).bit_length() gives 1
        x = (n ^ (n - 1)).bit_length() + 1
        if x & 1 == 0:
            value = 1 - value  # Bit index is even, so toggle value
        yield value


if __name__ == '__main__':
    run(6, p2_d06, '2')
