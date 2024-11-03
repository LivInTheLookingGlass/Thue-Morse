from itertools import count
from math import ceil, floor
from typing import Iterator, List, Optional, cast

from bitarray import bitarray

from ..args import run


def b(n: int, memo: bitarray) -> int:
    if (n << 1) < len(memo):
        result = tuple(memo[n << 1:(n + 1) << 1])
        match result:
            case (1, x):
                return -x
            case (0, 1):
                return 1
    n2 = n / 2
    result = b(ceil(n2), memo) - b(floor(n2), memo)
    if (n << 1) < len(memo):
        if result == 1:
            memo[n << 1:(n + 1) << 1] = bitarray((0, 1))
        else:
            memo[n << 1:(n + 1) << 1] = bitarray((1, abs(result)))
    return result


def p2_d07(_: int = 2) -> Iterator[int]:
    memo = bitarray((1, 0, 0, 1) + (0, ) * 28)
    for i in count(1):
        if i < (1 << 20):
            memo.extend((0, 0))
        yield (1 - b(2 * i - 1, memo)) // 2


if __name__ == '__main__':
    run(7, p2_d07, '2')
