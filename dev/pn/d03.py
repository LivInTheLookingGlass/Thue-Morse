from typing import Iterator

from ..args import run


def pn_d03(n: int = 2) -> Iterator[int]:
    if n < 2 or n > 256:
        raise ValueError("Due to memory use optimizations, this iterator only supports bases 2 thru 256")
    seq = bytearray(range(n))
    yield from seq
    while True:
        yield from ((x + i) % n for i in range(1, n) for x in seq)
        seq.extend((x + i) % n for i in range(1, n) for x in seq)


if __name__ == '__main__':
    run(3, pn_d03, 'n')
