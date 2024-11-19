from itertools import count
from typing import Callable, Iterator, Union

try:
    from z3 import If, Int, IntSort, RecAddDefinition, RecFunction
except ImportError:
    pass

from ..args import run
from ..compat.fluidpythran import boost
from ..compat.numba import jit


@boost
def get_p(n: int) -> Callable[[int, int], int]:
    if isinstance(n, int):
        if n > 1:
            return pip
        return pin
    raise ValueError("Invalid base")


@jit
def pip(x: int, n: int):
    """Digit sum for positive integer bases"""
    digit_sum = 0
    while x:
        digit_sum += x % n
        x //= n
    return digit_sum % n


@jit
def pin(x: int, n: int):
    """Digit sum for negative integer bases"""
    digit_sum = 0
    while x:
        digit = x % n
        quotient = x // n
        if digit < 0:
            digit += abs(n)
            quotient += 1
        digit_sum += digit
        x = quotient
    return digit_sum % abs(n)


@boost
def pn_d01(n: int = 2) -> Iterator[int]:
    p = get_p(n)
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
