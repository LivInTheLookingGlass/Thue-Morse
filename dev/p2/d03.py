from itertools import islice
from typing import Dict, Iterator, Union

try:
    from z3 import (Concat, If, Int, IntSort, Length, RecAddDefinition, RecFunction, String, StringSort, StringVal,
                    SubString)
except ImportError:
    pass

from ..args import bitarray, run


def p2_d03(_: int = 2) -> Iterator[int]:
    seq: bitarray = bitarray((0, 1))
    yield from seq
    while True:
        yield from (0 if x else 1 for x in islice(seq, len(seq)))
        seq.extend(0 if x else 1 for x in islice(seq, len(seq)))


def to_z3(_: Union[int, 'Int'] = 2) -> Dict[str, 'RecFunction']:
    n = Int('n')
    s = String('s')
    t = RecFunction('t2_03', IntSort(), StringSort())
    invert = RecFunction('invert2_03', StringSort(), StringSort())
    ilog2 = RecFunction('ilog2_2_03', IntSort(), IntSort())
    T2_03 = RecFunction('T2_03', IntSort(), IntSort())
    RecAddDefinition(invert, [s], If(s == StringVal(""), StringVal(""),
                                     If(s == StringVal("1"), StringVal("0"),
                                        If(s == StringVal("0"), StringVal("1"),
                                           Concat(invert(SubString(s, 0, 1)),
                                                  invert(SubString(s, 1, Length(s) - 1)))))))
    RecAddDefinition(t, [n], If(n == 0, StringVal('0'),
                                Concat(t(n - 1), invert(t(n - 1)))))
    RecAddDefinition(ilog2, [n], If(n <= 1, 0,
                                    1 + ilog2(n / 2)))
    RecAddDefinition(T2_03, [n], If(SubString(t(ilog2(n) + 1), n, 1) == StringVal("0"), 0, 1))
    return {'t': t, 'invert': invert, 'ilog2': ilog2, 'T': T2_03}


if __name__ == '__main__':
    run(3, p2_d03, '2')
