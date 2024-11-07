from itertools import count
from typing import Iterator

from ..args import run


def p(x: int, n: int) -> int:
    digit_sum = 0
    while x:
        digit_sum += x % n
        x //= n
    return digit_sum % n


def pn_d01(n: int = 2) -> Iterator[int]:
    for x in count():
        yield p(x, n)


if __name__ == '__main__':
    run(1, pn_d01, 'N')
