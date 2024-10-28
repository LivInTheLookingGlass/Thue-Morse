from itertools import count
from math import ceil, log
from typing import Iterator

from .args import run


def xor_in_n(a, b, n):
    if min(a, b) < 1:
        return max(a, b)
    res = 0
    ni = 1
    for _ in range(ceil(log(max(a, b), n)) + 1):
        res += (((a // ni) - (b // ni)) % n) * ni
        ni *= n
    return res


def seq_pn_d05(n: int = 2) -> Iterator[int]:
    yield from (0, 1)
    value = 1
    for x in count(2):
        value = int(log(xor_in_n(x, (x - 1), n), n) + value + 1) % n
        yield value


if __name__ == '__main__':
    run(5, seq_pn_d05, 'N')
