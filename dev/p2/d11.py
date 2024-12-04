from itertools import count
from typing import Generator, Union

try:
    from z3 import If, Int, IntSort, RecAddDefinition, RecFunction
except ImportError:
    pass

from ..args import run
from ..compat.fluidpythran import boost
from ..compat.int import bit_count


@boost
def odious() -> Generator[int, None, None]:
    for i in count():
        if bit_count(i) & 1:
            yield i


@boost
def p2_d11(_: int = 2) -> Generator[int, None, None]:
    yield from map(lambda x: (x + 1) & 1, odious())


def to_z3(_: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    f = RecFunction('f2_11', IntSort(), IntSort())
    p = RecFunction('p2_11', IntSort(), IntSort())
    o = RecFunction('o2_11', IntSort(), IntSort())
    T2_11 = RecFunction('T2_11', IntSort(), IntSort())
    RecAddDefinition(p, [n], If(n == 0, 0,
                                p(n / 2) + n))
    RecAddDefinition(f, [n], If(p(n) % 2 == 1, n,
                                f(n + 1)))
    RecAddDefinition(o, [n], If(n == 0, 1,
                                f(o(n - 1) + 1)))
    RecAddDefinition(T2_11, [n], (o(n) + 1) % 2)
    return T2_11


if __name__ == '__main__':
    run(11, p2_d11, '2')
