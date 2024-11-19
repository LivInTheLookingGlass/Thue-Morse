from collections import deque
from itertools import count
from multiprocessing import Pool, cpu_count
from multiprocessing.pool import ApplyResult
from typing import Deque, Iterator, Union

try:
    from z3 import If, Int, IntSort, RecAddDefinition, RecFunction
except ImportError:
    pass

from ..args import run
from ..compat.fluidpythran import boost
from ..compat.gmpy2 import mpz

max_size = 4 * cpu_count()


@boost
def gould(n: int) -> int:
    binomial_coeff = mpz(1)
    partial_sum = 0
    for k in range((n + 1) >> 1):
        # Add the current term to the total sum
        partial_sum += binomial_coeff & 1
        # C(n, k) = C(n, k-1) * (n - (k - 1)) / k
        binomial_coeff = binomial_coeff * (n - k) // (k + 1)
    partial_sum <<= 1
    if (n & 1) == 0:
        partial_sum += binomial_coeff & 1
    return int((partial_sum - 1) % 3)  # This isn't part of the gould sequence, but it helps to process this here


@boost
def p2_d13(_: int = 2) -> Iterator[int]:
    queue: Deque[ApplyResult[int]] = deque(maxlen=max_size)
    with Pool() as pool:
        for i in count():
            queue.append(pool.apply_async(gould, (i,)))
            if len(queue) >= max_size:
                yield queue.popleft().get()  # Blocking call to get the result


def to_z3(_: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    k = Int('k')
    binomial_coeff = RecFunction('binomial_coeff2_13', IntSort(), IntSort(), IntSort())
    partial_sum = RecFunction('partial_sum2_13', IntSort(), IntSort(), IntSort())
    gould = RecFunction('gould2_13', IntSort(), IntSort())
    T2_13 = RecFunction('T2_13', IntSort(), IntSort())
    RecAddDefinition(gould, [n], If(n % 2 == 0, partial_sum(n, 0) * 2 + binomial_coeff(n, n / 2) % 2,
                                    partial_sum(n, 0) * 2))
    RecAddDefinition(binomial_coeff, [n, k], If(k == 0, 1,
                                                binomial_coeff(n, k - 1) * (n - (k - 1)) / k))
    RecAddDefinition(partial_sum, [n, k], If(k > (n + 1) / 2, 0,
                                             If(binomial_coeff(n, k) % 2 == 1, 1 + partial_sum(n, k + 1),
                                                partial_sum(n, k + 1))))
    RecAddDefinition(T2_13, [n], (gould(n) - 1) % 3)
    return T2_13


if __name__ == '__main__':
    run(13, p2_d13, '2')
