from itertools import islice
from typing import Iterator

from ..args import bitarray, run


def p2_d03(_: int = 2) -> Iterator[int]:
    seq: bitarray = bitarray((0, 1))
    yield from seq
    while True:
        yield from (0 if x else 1 for x in islice(seq, len(seq)))
        seq.extend(0 if x else 1 for x in islice(seq, len(seq)))


if __name__ == '__main__':
    run(3, p2_d03, '2')
