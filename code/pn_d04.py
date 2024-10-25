from itertools import count
from typing import Iterator

from .args import run


def T(x: int, n: int) -> int:
    if x == 0:
        return 0
    return (x + T(x // n, n)) % n


def seq_pn_d04(n: int = 2) -> Iterator[int]:
    for i in count():
        yield T(i, n)


if __name__ == '__main__':
    args = run(4, seq_pn_d04, 'n')
