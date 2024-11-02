from itertools import count
from math import ceil, floor
from typing import Iterator, List, Optional, cast

from ..args import run


def b(n: int, memo: List[Optional[int]]) -> int:
    if n < len(memo) and memo[n] is not None:
        return cast(int, memo[n])
    n2 = n / 2
    result = b(ceil(n2), memo) - b(floor(n2), memo)
    if n < len(memo):
        memo[n] = result
    return result


def p2_d07(_: int = 2) -> Iterator[int]:
    memo: List[Optional[int]] = [0, 1]
    for i in count(1):
        if i < (1 << 20):
            memo.extend((None, None))
        yield (1 - b(2 * i - 1, memo)) // 2


if __name__ == '__main__':
    run(7, p2_d07, '2')
