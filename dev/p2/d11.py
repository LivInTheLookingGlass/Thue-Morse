from itertools import count
from typing import Dict, Iterator, Union

try:
    from z3 import If, Int, IntSort, RecAddDefinition, RecFunction
except ImportError:
    pass

from ..args import run


def A1510481(n):
    n1 = n + 1
    return (n1 >> 1) + ((n1.bit_count() & 1) * (n1 & 1))


def p2_d11(_: int = 2) -> Iterator[int]:
    for i in count():
        yield 1 - A1510481(i) + A1510481(i - 1)


def to_z3(_: Union[int, 'Int'] = 2) -> Dict[str, 'RecFunction']:
    n = Int('n')
    ilog2 = RecFunction('ilog2_2_11', IntSort(), IntSort())
    p = RecFunction('p2_11', IntSort(), IntSort())
    T2_11 = RecFunction('T2_11', IntSort(), IntSort())
    RecAddDefinition(ilog2, [n], If(n <= 1, 0,
                                    1 + ilog2(n / 2)))
    RecAddDefinition(p, [n], n / 2 + (ilog2(n + 1) % 2) * (n % 2))
    RecAddDefinition(T2_11, [n], 1 - p(n + 1) + p(n))
    return {'ilog2': ilog2, 'p': p, 'T': T2_11}


if __name__ == '__main__':
    run(11, p2_d11, '2')
