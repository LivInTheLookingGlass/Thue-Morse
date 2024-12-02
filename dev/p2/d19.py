from itertools import count
from typing import Generator

from ..args import run
from ..compat.fluidpythran import boost
from ..compat.int import bit_count


@boost
def p2_d19(_: int = 2) -> Generator[int, None, None]:
    yield 0
    for i in count():
        for x in reversed(range(1 << i, 1 << (i + 1))):
            yield 1 - ((x.bit_length() - bit_count(x)) & 1)


if __name__ == '__main__':
    run(19, p2_d19, '2')
