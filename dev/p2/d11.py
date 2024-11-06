from itertools import chain
from typing import Iterator

from ..args import run
from .d08 import odious
from .d09 import evil


def p2_d11(_: int = 2) -> Iterator[int]:
    for i in chain.from_iterable(zip(odious(), evil())):
        yield 1 - i & 1


if __name__ == '__main__':
    run(11, p2_d11, '2')
