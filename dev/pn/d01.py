from itertools import count
from typing import Iterator, Union

try:
    from z3 import If, Int, IntSort, RecAddDefinition, RecFunction
except ImportError:
    pass

from ..args import run
from ..compat.numba import jit


@jit
def p(x: int, n: int) -> int:
    digit_sum = 0
    while x:
        digit_sum += x
        digit_sum %= n
        x //= n
    return digit_sum


def pn_d01(n: int = 2) -> Iterator[int]:
    return (p(x, n) for x in count())


def to_z3(s: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    ps = RecFunction('pn_01', IntSort(), IntSort())
    Tn_01 = RecFunction('Tn_01', IntSort(), IntSort())
    RecAddDefinition(ps, [n], If(n == 0, 0,
                                 ps(n / s) + n))
    RecAddDefinition(Tn_01, [n], ps(n) % s)
    return Tn_01


if __name__ == '__main__':
    run(1, pn_d01, 'n')
