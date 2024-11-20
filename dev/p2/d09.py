from itertools import count
from typing import Iterator, Union

try:
    from z3 import If, Int, IntSort, RecAddDefinition, RecFunction
except ImportError:
    pass

from ..args import run
from ..compat.fluidpythran import boost


@boost
def odious() -> Iterator[int]:
    for i in count():
        if i.bit_count() & 1:
            yield i


@boost
def p2_d09(_: int = 2) -> Iterator[int]:
    for i in odious():
        yield (i + 1) & 1


def to_z3(_: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    f = RecFunction('f2_09', IntSort(), IntSort())
    p = RecFunction('p2_09', IntSort(), IntSort())
    o = RecFunction('o2_09', IntSort(), IntSort())
    T2_09 = RecFunction('T2_09', IntSort(), IntSort())
    RecAddDefinition(p, [n], If(n == 0, 0,
                                p(n / 2) + n))
    RecAddDefinition(f, [n], If(p(n) % 2 == 1, n,
                                f(n + 1)))
    RecAddDefinition(o, [n], If(n == 0, 1,
                                f(o(n - 1) + 1)))
    RecAddDefinition(T2_09, [n], (o(n) + 1) % 2)
    return T2_09


if __name__ == '__main__':
    run(9, p2_d09, '2')
