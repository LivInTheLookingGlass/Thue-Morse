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
def evil(_: int = 2) -> Generator[int, None, None]:
    for i in count():
        if not (bit_count(i) & 1):
            yield i


@boost
def p2_d12(_: int = 2, size_hint: Optional[int] = None) -> Generator[int, None, None]:
    yield from map(lambda n, i: (i - (n << 1)) & 1, count(), evil())


def to_z3(_: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    f = RecFunction('f2_12', IntSort(), IntSort())
    p = RecFunction('p2_12', IntSort(), IntSort())
    e = RecFunction('e2_12', IntSort(), IntSort())
    T2_12 = RecFunction('T2_12', IntSort(), IntSort())
    RecAddDefinition(p, [n], If(n == 0, 0,
                                p(n / 2) + n))
    RecAddDefinition(f, [n], If(p(n) % 2 == 0, n,
                                f(n + 1)))
    RecAddDefinition(e, [n], If(n == 0, 0,
                                f(e(n - 1) + 1)))
    RecAddDefinition(T2_12, [n], (e(n) + 1) % 2)
    return T2_12


if __name__ == '__main__':
    run(12, p2_d12, '2')
