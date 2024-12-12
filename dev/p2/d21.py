from itertools import count
from operator import mul
from typing import Generator, Optional

import numpy as np

from ..args import run
from ..compat.fluidpythran import boost


@boost
def p2_d21(
    _: int = 2,
    size_hint: Optional[int] = None,
    benchmark: bool = False
) -> Generator[int, None, None]:
    p = 10
    remaining_prob = 1.0
    players = np.array([0.0, 0.0], np.float64)
    for x in count():
        value = remaining_prob / (1 << p)
        player = np.argmin(players)
        players[player] += value
        remaining_prob -= value
        yield player


if __name__ == '__main__':
    run(21, p2_d21, '2')
