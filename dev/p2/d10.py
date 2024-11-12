from itertools import count
from typing import Dict, Iterator, Union

try:
    from z3 import If, Int, IntSort, RecAddDefinition, RecFunction
except ImportError:
    pass

from ..args import run


def evil(_: int = 2) -> Iterator[int]:
    for i in count():
        if i.bit_count() & 1 == 0:
            yield i


def p2_d10(_: int = 2) -> Iterator[int]:
    for n, i in enumerate(evil()):
        yield (i - (n << 1)) & 1


def to_z3(_: Union[int, 'Int'] = 2) -> Dict[str, 'RecFunction']:
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
    return {'f': f, 'p': p, 'e': e, 'T': T2_10}


if __name__ == '__main__':
    run(10, p2_d10, '2')
