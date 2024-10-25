from itertools import count
from typing import Iterator

from .args import run


def T(n: int) -> int:
    if n == 0:
        return 0
    return (n - T(n // 2)) % 2


def seq_p2_d04(_: int = 2) -> Iterator[int]:
    for i in count():
        yield T(i)


if __name__ == '__main__':
    args = run(4, seq_p2_d04, '2')
