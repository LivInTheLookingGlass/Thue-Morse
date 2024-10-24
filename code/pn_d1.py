from functools import reduce
from itertools import count
from typing import Iterator

from .args import run


def seq_pn_d1(p: int = 2) -> Iterator[int]:
    for x in count():
        digit_sum = 0
        while x:
            digit_sum += x % p
            x //= p
        yield digit_sum % p


if __name__ == '__main__':
    args = run(1, seq_pn_d1, 'N')
