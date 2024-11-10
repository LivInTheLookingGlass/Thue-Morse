from itertools import count
from typing import Dict, Iterator, Union

try:
    from z3 import Function, Int, IntSortRecAddDefinition, RecFunction
except ImportError:
    pass

from ..args import run


def p2_d01(_: int = 2) -> Iterator[int]:
    for x in count():
        yield x.bit_count() & 1


def to_z3() -> Dict[str, Union['Function', 'RecFunction']]:
    n = Int('n')
    p = RecFunction('p', IntSort(), IntSort())
    T2_01 = RecFunction('T2_01', IntSort(), IntSort())
    RecAddDefinition(p, [n], If(n == 0, 0, (p(n / 2) + n)))
    RecAddDefinition(T2_01, [n], p(n) % 2)
    return {
        'p': p,
        'T2_01': T2_01
    }


if __name__ == '__main__':
    run(1, p2_d01, '2')
