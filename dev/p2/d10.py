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
def evil(_: int = 2) -> Generator[int, None, None]:
    for i in count():
        if not (bit_count(i) & 1):
            yield i


@boost
def p2_d10(_: int = 2) -> Generator[int, None, None]:
    yield from map(lambda n, i: (i - (n << 1)) & 1, count(), evil())


def to_z3(_: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    f = RecFunction('f2_10', IntSort(), IntSort())
    p = RecFunction('p2_10', IntSort(), IntSort())
    e = RecFunction('e2_10', IntSort(), IntSort())
    T2_10 = RecFunction('T2_10', IntSort(), IntSort())
    RecAddDefinition(p, [n], If(n == 0, 0,
                                p(n / 2) + n))
    RecAddDefinition(f, [n], If(p(n) % 2 == 0, n,
                                f(n + 1)))
    RecAddDefinition(e, [n], If(n == 0, 0,
                                f(e(n - 1) + 1)))
    RecAddDefinition(T2_10, [n], (e(n) + 1) % 2)
    return T2_10


if __name__ == '__main__':
    run(10, p2_d10, '2')
