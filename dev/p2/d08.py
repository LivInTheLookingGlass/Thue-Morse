from typing import Generator, Union

try:
    from z3 import (Concat, If, Int, IntSort, Length, RecAddDefinition, RecFunction, String, StringSort, StringVal,
                    SubString)
except ImportError:
    pass

from ..args import run
from ..compat.bitarray import bitarray
from ..compat.fluidpythran import boost


@boost
def p2_d08(_: int = 2) -> Generator[int, None, None]:
    seq: bitarray = bitarray((0, 1))
    yield from seq
    while True:
        extension = seq.copy()
        extension.invert()
        yield from extension
        seq.extend(extension)


def to_z3(_: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    s = String('s')
    t = RecFunction('t2_08', IntSort(), StringSort())
    invert = RecFunction('invert2_08', StringSort(), StringSort())
    ilog2 = RecFunction('ilog2_2_08', IntSort(), IntSort())
    T2_08 = RecFunction('T2_08', IntSort(), IntSort())
    RecAddDefinition(invert, [s], If(s == StringVal(""), StringVal(""),
                                     If(s == StringVal("1"), StringVal("0"),
                                        If(s == StringVal("0"), StringVal("1"),
                                           Concat(invert(SubString(s, 0, 1)),
                                                  invert(SubString(s, 1, Length(s) - 1)))))))
    RecAddDefinition(t, [n], If(n == 0, StringVal('0'),
                                Concat(t(n - 1), invert(t(n - 1)))))
    RecAddDefinition(ilog2, [n], If(n <= 1, 0,
                                    1 + ilog2(n / 2)))
    RecAddDefinition(T2_08, [n], If(SubString(t(ilog2(n) + 1), n, 1) == StringVal("0"), 0, 1))
    return T2_08


if __name__ == '__main__':
    run(8, p2_d08, '2')
