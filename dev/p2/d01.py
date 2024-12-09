from itertools import count
from typing import Generator, Optional, Union

try:
    from z3 import If, Int, IntSort, RecAddDefinition, RecFunction
except ImportError:
    pass

from ..args import run
from ..compat.fluidpythran import boost
from ..compat.int import bit_count


@boost
def p2_d01(_: int = 2, size_hint: Optional[int] = None) -> Generator[int, None, None]:
    yield from map(lambda x: bit_count(x) & 1, count())


def to_z3(_: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    p = RecFunction('p2_01', IntSort(), IntSort())
    T2_01 = RecFunction('T2_01', IntSort(), IntSort())
    RecAddDefinition(p, [n], If(n == 0, 0,
                                p(n / 2) + n))
    RecAddDefinition(T2_01, [n], p(n) % 2)
    return T2_01


if __name__ == '__main__':
    run(1, p2_d01, '2')
