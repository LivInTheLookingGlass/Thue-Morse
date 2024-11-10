from itertools import count
from typing import Dict, Iterator, Union

try:
    from z3 import Function, Int, IntSortRecAddDefinition, RecFunction
except ImportError:
    pass

from ..args import run


def T(n: int) -> int:
    if n == 0:
        return 0
    return (n - T(n >> 1)) & 1


def p2_d06(_: int = 2) -> Iterator[int]:
    for i in count():
        yield T(i)


if __name__ == '__main__':
    run(6, p2_d06, '2')


def to_z3(_: Union[int, 'Int'] = 2) -> Dict[str, Union['Function', 'RecFunction']]:
    n = Int('n')
    p = RecFunction('p', IntSort(), IntSort())
    T2_06 = RecFunction('T2_06', IntSort(), IntSort())
    RecAddDefinition(p, [n], If(n == 0, 0, (n - p(n / 2) % 2)))
    RecAddDefinition(T2_01, [n], p(n))
    return {
        'p': p,
        'T2_06': T2_06
    }


if __name__ == '__main__':
    run(1, p2_d01, '2')
