from itertools import tee
from typing import Iterable, Iterator, Tuple, TypeVar

from pytest import mark

from .compat.fluidpythran import boost
from .pn.d01 import pn_d01

T = TypeVar("T")
test_len = 1 << 10


@boost
def groupwise(iterable: Iterable[T], size: int) -> Iterator[Tuple[T, ...]]:
    """Iterate over something in buckets of a given size."""
    iters = tee(iterable, size)
    for idx, x in enumerate(iters):
        for _ in range(idx):
            next(x, None)
    return zip(*iters)


@boost
def is_sorta_square_free(iterator, b: int, n: int) -> bool:
    len_to_check = n // 2
    for k in range(1, len_to_check + 1):
        iter1, iter2 = tee(groupwise(iterator(), b), 2)
        sliding_window1 = groupwise(iter1, k)  # for windows of size k
        sliding_window2 = groupwise(iter2, k)
        for _ in range(k):
            next(sliding_window2)
        for idx, first, second in zip(range(len_to_check + 1 - k), sliding_window1, sliding_window2):
            if first == second:
                print(idx, first, second)
                return False
    return True


@boost
def is_cube_free(iterator, b: int, n: int) -> bool:
    len_to_check = n // 3
    for k in range(2, len_to_check + 1):
        iter1, iter2, iter3 = tee(iterator(), 3)
        sliding_window1 = groupwise(iter1, k)  # for windows of size k
        sliding_window2 = groupwise(iter2, k)
        sliding_window3 = groupwise(iter3, k)
        for _ in range(k):
            next(sliding_window2)
        for _ in range(k * 2):
            next(sliding_window3)
        for idx, first, second, third in zip(
            range(len_to_check + 1 - k),
            sliding_window1,
            sliding_window2,
            sliding_window3
        ):
            if first == second and second == third:
                print(idx, first, second, third)
                return False
    return True


@boost
def is_overlap_free(iterator, b: int, n: int) -> bool:
    len_to_check = (n - 1) // 2
    for k in range(2, len_to_check + 1):
        iter1, iter2 = tee(iterator(), 2)
        sliding_window1 = groupwise(iter1, k)  # for windows of size k
        sliding_window2 = groupwise(iter2, k + 1)
        for _ in range(k):
            next(sliding_window2)
        for idx, first, second in zip(range(len_to_check + 1 - k), sliding_window1, sliding_window2):
            start = first[0:]
            if (first + start) == second:
                print(idx, first, second)
                return False
    return True


@mark.parametrize("b", range(2, test_len >> 4))
@boost
def test_pairwise_square_free(b: int):
    n = b
    while n < test_len:
        n *= b
    assert is_sorta_square_free(lambda: pn_d01(b, n), 2, n)


@mark.parametrize("b", range(2, test_len >> 4))
@boost
def test_groupwise_square_free(b: int):
    n = b
    while n < test_len:
        n *= b
    assert is_sorta_square_free(lambda: pn_d01(b, n), b, n)


@mark.parametrize("b", range(2, 1025))
@boost
def test_overlap_free(b: int):
    n = b
    while n < test_len:
        n *= b
    assert is_overlap_free(lambda: pn_d01(b, n), b, n)


@mark.parametrize("b", range(2, 1025))
@boost
def test_cube_free(b: int):
    n = b
    while n < test_len:
        n *= b
    assert is_cube_free(lambda: pn_d01(b, n), b, n)
