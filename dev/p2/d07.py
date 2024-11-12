from itertools import count
from typing import Dict, Iterator, Union

try:
    from z3 import If, Int, IntSort, RecAddDefinition, RecFunction
except ImportError:
    pass

from ..args import run


def p2_d07(_: int = 2) -> Iterator[int]:
    value = 1
    for n in count():
        # Note: assumes that (-1).bit_length() gives 1
        x = (n ^ (n - 1)).bit_length() + 1
        if x & 1 == 0:
            value = 1 - value  # Bit index is even, so toggle value
        yield value


def to_z3(_: Union[int, 'Int'] = 2) -> Dict[str, 'RecFunction']:
    n = Int('n')
    x = Int('x')
    y = Int('y')
    ilog2 = RecFunction('ilog2_2_07', IntSort(), IntSort())
    xor = RecFunction('xor_2_07', IntSort(), IntSort(), IntSort())
    p = RecFunction('p2_07', IntSort(), IntSort())
    T2_07 = RecFunction('T2_07', IntSort(), IntSort())
    RecAddDefinition(xor, [x, y], If(x == 0, y,
                                     If(y == 0, x,
                                        ((x % 2) + (y % 2)) % 2 + 2 * xor(x / 2, y / 2))))
    RecAddDefinition(ilog2, [n], If(n <= 1, 0,
                                    1 + ilog2(n / 2)))
    RecAddDefinition(p, [n], ilog2(xor(n, (n - 1))) + 1)
    RecAddDefinition(T2_07, [n], If(n == 0, 0,
                                    If(p(n) % 2 == 0, 1 - T2_07(n - 1),
                                       T2_07(n - 1))))
    return {'ilog2': ilog2, 'xor': xor, 'p': p, 'T': T2_07}


if __name__ == '__main__':
    run(7, p2_d07, '2')
