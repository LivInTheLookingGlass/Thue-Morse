from itertools import chain
from typing import Iterator

from ..args import run
from .d09 import odious
from .d10 import evil


def p2_d12(_: int = 2) -> Iterator[int]:
    for i in chain.from_iterable(zip(odious(), evil())):
        yield 1 - i & 1


if __name__ == '__main__':
    run(12, p2_d12, '2')
