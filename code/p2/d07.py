from itertools import count
from math import ceil, floor
from typing import Iterator, List, Optional

from ..args import run


def b(n: int, memo: List[Optional[int]]) -> int:
    if memo[n] is None:
        n2 = n / 2
        memo[n] = b(ceil(n2), memo) - b(floor(n2), memo)
    return memo[n]


def p2_d07(_: int = 2) -> Iterator[int]:
    memo: List[Optional[int]] = [0, 1]
    for i in count(1):
        memo.extend((None, None))
        yield (1 - b(2 * i - 1, memo)) // 2


if __name__ == '__main__':
    run(7, p2_d07, '2')
