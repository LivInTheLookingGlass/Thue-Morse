from itertools import count
from math import log
from typing import Iterator

from ..args import run


def xor_in_n(a, b, n):
    if min(a, b) < 1:
        return max(a, b)
    res = 0
    ni = 1
    while a > 0 or b > 0:
        a_digit = a % n
        b_digit = b % n
        res += ((a_digit - b_digit) % n) * ni
        a //= n
        b //= n
        ni *= n
    return res


def seq_pn_d06(n: int = 2) -> Iterator[int]:
    yield from (0, 1)
    value = 1
    for x in count(2):
        value = int(log(xor_in_n(x, (x - 1), n), n) + value + 1) % n
        yield value


if __name__ == '__main__':
    run(6, seq_pn_d06, 'N')
