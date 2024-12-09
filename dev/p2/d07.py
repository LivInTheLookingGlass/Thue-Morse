from itertools import count
from typing import Generator, Optional

from ..args import run
from ..compat.fluidpythran import boost
from ..compat.int import bit_count


@boost
def p2_d07(_: int = 2, size_hint: Optional[int] = None) -> Generator[int, None, None]:
    yield 0
    for i in count():
        for x in reversed(range(1 << i, 1 << (i + 1))):
            yield 1 - ((x.bit_length() - bit_count(x)) & 1)


if __name__ == '__main__':
    run(7, p2_d07, '2')
