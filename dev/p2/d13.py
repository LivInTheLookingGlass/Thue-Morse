from collections import deque
from itertools import count
from multiprocessing import Pool, cpu_count
from multiprocessing.pool import ApplyResult
from typing import Deque, Iterator

from ..args import run

max_size = 4 * cpu_count()


def gould(n: int) -> int:
    binomial_coeff = 1
    partial_sum = 0
    for k in range((n + 1) >> 1):
        # Add the current term to the total sum
        partial_sum += binomial_coeff & 1
        # C(n, k) = C(n, k-1) * (n - (k - 1)) / k
        binomial_coeff = binomial_coeff * (n - k) // (k + 1)
    partial_sum <<= 1
    if (n & 1) == 0:
        partial_sum += binomial_coeff & 1
    return partial_sum


def p2_d13(_: int = 2) -> Iterator[int]:
    queue: Deque[ApplyResult[int]] = deque(maxlen=max_size)
    with Pool() as pool:
        for i in count():
            queue.append(pool.apply_async(gould, (i,)))
            if len(queue) >= max_size:
                yield (queue.popleft().get() - 1) % 3  # Blocking call to get the result


if __name__ == '__main__':
    run(13, p2_d13, '2')
