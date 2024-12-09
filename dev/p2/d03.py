from functools import partial
from itertools import count
from typing import Generator, Optional, Union

import numpy as np

try:
    from z3 import If, Int, IntSort, RecAddDefinition, RecFunction, ToInt
except ImportError:
    pass

from ..args import run
from ..compat.fluidpythran import boost
from ..compat.int import bit_count
from ..pn.d02 import closest_root


@boost
def p2_d03(
    _: int = 2,
    size_hint: Optional[int] = None,
    benchmark: bool = False
) -> Generator[int, None, None]:
    func = partial(closest_root, roots=np.array([1, -1]))
    yield from map(lambda x: func((-1)**bit_count(x)), count())


def to_z3(_: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    p = RecFunction('p2_02', IntSort(), IntSort())
    T2_02 = RecFunction('T2_02', IntSort(), IntSort())
    RecAddDefinition(p, [n], If(n == 0, 0,
                                p(n / 2) + (n % 2)))
    RecAddDefinition(T2_02, [n], ToInt((1 - (-1)**p(n)) / 2))
    return T2_02


if __name__ == '__main__':
    run(3, p2_d03, '2')
