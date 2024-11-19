from itertools import count
from typing import Iterator, Union

try:
    from z3 import If, Int, IntSort, RecAddDefinition, RecFunction
except ImportError:
    pass

from ..args import run
from ..compat.bitarray import bitarray
from ..compat.fluidpythran import boost


@boost
def b(n: int, memo: bitarray) -> int:
    nr1 = n << 1
    nr1p1 = nr1 + 1
    lmemo = len(memo)
    if nr1p1 < lmemo:
        if memo[nr1] == 1:
            return -memo[nr1p1]
        elif memo[nr1p1] == 1:
            return 1
    n2 = n >> 1
    result = b(n2 + (n & 1), memo) - b(n2, memo)
    if nr1p1 < lmemo:
        memo[nr1] = (result < 1)
        memo[nr1p1] = abs(result)
    return result


@boost
def p2_d08(_: int = 2) -> Iterator[int]:
    mem_limit = 1 << 20
    memo = bitarray(1024)
    memo[:4] = bitarray((1, 0, 0, 1))
    for i in count(1):
        if i < mem_limit:
            memo.extend((0, 0))
        yield (1 - b((i << 1) - 1, memo)) >> 1


def to_z3(_: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    b = RecFunction('b2_08', IntSort(), IntSort())
    T2_08 = RecFunction('T2_08', IntSort(), IntSort())
    RecAddDefinition(b, [n], If(n < 2, n,
                                b(n / 2 + (n % 2)) - b(n / 2)))
    RecAddDefinition(T2_08, [n], b(n) % 2)
    return T2_08


if __name__ == '__main__':
    run(8, p2_d08, '2')
