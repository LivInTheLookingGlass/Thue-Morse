from itertools import count
from typing import Dict, Iterator, Union

try:
    from z3 import Function, Int, IntSortRecAddDefinition, RecFunction
except ImportError:
    pass

from ..args import run


def p2_d02(_: int = 2) -> Iterator[int]:
    for x in count():
        yield (1 - (-1)**(x.bit_count())) >> 1


def to_z3(_: Union[int, 'Int'] = 2) -> Dict[str, Union['Function', 'RecFunction']]:
    n = Int('n')
    p = RecFunction('p', IntSort(), IntSort())
    T2_02 = RecFunction('T2_02', IntSort(), IntSort())
    RecAddDefinition(p, [n], If(n == 0, 0, (p(n / 2) + (n % 2))))
    RecAddDefinition(T2_02, [n], (1 - (-1)**p(n)) / 2)
    return {
        'p': p,
        'T2_02': T2_02
    }


if __name__ == '__main__':
    run(1, p2_d02, '2')


