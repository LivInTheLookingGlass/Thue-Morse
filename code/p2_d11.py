from itertools import chain
from typing import Iterator

from .args import run
from .p2_d08 import odious
from .p2_d09 import evil


def seq_p2_d11(_: int = 2) -> Iterator[int]:
    for i in chain.from_iterable(zip(odious(), evil())):
        yield 1 - i % 2


if __name__ == '__main__':
    run(11, seq_p2_d11, '2')
