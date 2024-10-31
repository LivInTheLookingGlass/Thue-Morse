from itertools import count
from typing import Iterator

from ..args import run


def pn_d01(p: int = 2) -> Iterator[int]:
    for x in count():
        digit_sum = 0
        while x:
            digit_sum += x % p
            x //= p
        yield digit_sum % p


if __name__ == '__main__':
    run(1, pn_d01, 'N')
