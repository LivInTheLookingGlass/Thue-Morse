from itertools import count
from typing import Dict, Iterator, Union

try:
    from z3 import Function, If, Int, IntSort, RecAddDefinition, RecFunction
except ImportError:
    pass

from ..args import run


def p(x: int, n: int) -> int:
    digit_sum = 0
    while x:
        digit_sum += x % n
        x //= n
    return digit_sum % n


def pn_d01(n: int = 2) -> Iterator[int]:
    for x in count():
        yield p(x, n)


def to_z3(s: Union[int, 'Int'] = 2) -> Dict[str, Union['Function', 'RecFunction']]:
    n = Int('n')
    ps = RecFunction('ps', IntSort(), IntSort())
    Tn_01 = RecFunction('Tn_01', IntSort(), IntSort())
    RecAddDefinition(ps, [n], If(n == 0, 0, (ps(n / s) + n)))
    RecAddDefinition(Tn_01, [n], ps(n) % s)
    return {
        'p': p,
        'T': Tn_01
    }


if __name__ == '__main__':
    run(1, pn_d01, 'n')
