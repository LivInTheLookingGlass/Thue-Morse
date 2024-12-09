from atexit import register
from collections import deque
from itertools import count
from multiprocessing import cpu_count
from multiprocessing.pool import ApplyResult, Pool
from typing import Deque, Generator, Optional, Union

try:
    from z3 import If, Int, IntSort, RecAddDefinition, RecFunction
except ImportError:
    pass

from ..args import run
from ..compat.fluidpythran import boost
from ..compat.gmpy2 import mpz

max_size = 4 * cpu_count()
pool: Optional[Pool] = None


def ensure_pool():
    global pool
    if pool is None:
        pool = Pool()
        register(pool.close)


@boost
def gould(n: int) -> int:
    binomial_coeff = mpz(1)
    partial_sum = 0
    k = 0
    while k < ((n + 1) >> 1):
        # Add the current term to the total sum
        partial_sum += binomial_coeff & 1
        # C(n, k) = C(n, k-1) * (n - (k - 1)) / k
        binomial_coeff *= n - k
        k += 1
        binomial_coeff //= k
    partial_sum <<= 1
    if (n & 1) == 0:
        partial_sum += binomial_coeff & 1
    return int((partial_sum - 1) % 3)  # This isn't part of the gould sequence, but it helps to process this here


@boost
def p2_d15(_: int = 2, size_hint: Optional[int] = None) -> Generator[int, None, None]:
    queue: Deque[ApplyResult[int]] = deque(maxlen=max_size)
    ensure_pool()
    global pool
    assert pool is not None
    for i in count():
        queue.append(pool.apply_async(gould, (i,)))
        if len(queue) >= max_size:
            yield queue.popleft().get()  # Blocking call to get the result


def to_z3(_: Union[int, 'Int'] = 2) -> 'RecFunction':
    n = Int('n')
    k = Int('k')
    binomial_coeff = RecFunction('binomial_coeff2_15', IntSort(), IntSort(), IntSort())
    partial_sum = RecFunction('partial_sum2_15', IntSort(), IntSort(), IntSort())
    gould = RecFunction('gould2_15', IntSort(), IntSort())
    T2_15 = RecFunction('T2_15', IntSort(), IntSort())
    RecAddDefinition(gould, [n], If(n % 2 == 0, partial_sum(n, 0) * 2 + binomial_coeff(n, n / 2) % 2,
                                    partial_sum(n, 0) * 2))
    RecAddDefinition(binomial_coeff, [n, k], If(k == 0, 1,
                                                binomial_coeff(n, k - 1) * (n - (k - 1)) / k))
    RecAddDefinition(partial_sum, [n, k], If(k > (n + 1) / 2, 0,
                                             If(binomial_coeff(n, k) % 2 == 1, 1 + partial_sum(n, k + 1),
                                                partial_sum(n, k + 1))))
    RecAddDefinition(T2_15, [n], (gould(n) - 1) % 3)
    return T2_15


if __name__ == '__main__':
    run(15, p2_d15, '2')
