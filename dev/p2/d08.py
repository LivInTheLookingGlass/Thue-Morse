from itertools import count
from typing import Dict, Iterator, Union

try:
    from z3 import If, Int, IntSort, RecAddDefinition, RecFunction
except ImportError:
    pass

from ..args import bitarray, run


def b(n: int, memo: bitarray) -> int:
    nr1 = n << 1
    if (nr1) < len(memo):
        res = tuple(memo[nr1:(n + 1) << 1])
        match res:
            case (1, x):
                return -x
            case (0, 1):
                return 1
    n2 = n >> 1
    result = b(n2 + (n & 1), memo) - b(n2, memo)
    if nr1 < len(memo):
        if result == 1:
            memo[nr1:(n + 1) << 1] = bitarray((0, 1))
        else:
            memo[nr1:(n + 1) << 1] = bitarray((1, abs(result)))
    return result


def p2_d08(_: int = 2) -> Iterator[int]:
    mem_limit = 1 << 20
    memo = bitarray(1024)
    memo[:4] = bitarray((1, 0, 0, 1))
    for i in count(1):
        if i < mem_limit:
            memo.extend((0, 0))
        yield (1 - b((i << 1) - 1, memo)) >> 1


def to_z3(_: Union[int, 'Int'] = 2) -> Dict[str, 'RecFunction']:
    n = Int('n')
    b = RecFunction('b2_08', IntSort(), IntSort())
    T2_08 = RecFunction('T2_08', IntSort(), IntSort())
    RecAddDefinition(b, [n], If(n < 2, n,
                                b(n / 2 + (n % 2)) - b(n / 2)))
    RecAddDefinition(T2_08, [n], b(n) % 2)
    return {'b': b, 'T': T2_08}


if __name__ == '__main__':
    run(8, p2_d08, '2')
