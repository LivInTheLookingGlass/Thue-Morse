from itertools import tee
from typing import Iterable, Iterator, Tuple, TypeVar

from pytest import mark

from .pn.d01 import pn_d01

T = TypeVar("T")


def groupwise(iterable: Iterable[T], size: int) -> Iterator[Tuple[T, ...]]:
    """Iterate over something in buckets of a given size."""
    iters = tee(iterable, size)
    for idx, x in enumerate(iters):
        for _ in range(idx):
            next(x, None)
    return zip(*iters)


def is_sorta_square_free(iterator, b: int, n: int) -> bool:
    len_to_check = n // 2
    for k in range(b, len_to_check + 1, b):
        seq_iter = iterator()
        sliding_window1 = groupwise(seq_iter, k)  # for windows of size k
        sliding_window2 = groupwise(seq_iter, k)
        for _ in range(k):
            next(sliding_window2)
        for idx, first, second in zip(range(len_to_check + 1 - k), sliding_window1, sliding_window2):
            if first == second:
                print(idx, first, second)
                return False
    return True


def is_cube_free(iterator, b: int, n: int) -> bool:
    len_to_check = n // 3
    for k in range(2, len_to_check + 1):
        seq_iter = iterator()
        sliding_window1 = groupwise(seq_iter, k)  # for windows of size k
        sliding_window2 = groupwise(seq_iter, k)
        sliding_window3 = groupwise(seq_iter, k)
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


def is_overlap_free(iterator, b: int, n: int) -> bool:
    len_to_check = (n - 1) // 2
    for k in range(2, len_to_check + 1):
        seq_iter = iterator()
        sliding_window1 = groupwise(seq_iter, k)  # for windows of size k
        sliding_window2 = groupwise(seq_iter, k + 1)
        for _ in range(k):
            next(sliding_window2)
        for idx, first, second in zip(range(len_to_check + 1 - k), sliding_window1, sliding_window2):
            start = first[0:]
            if (first + start) == second:
                print(idx, first, second)
                return False
    return True


@mark.parametrize("b", range(2, 1025))
def test_sorta_square_free(b: int):
    n = b
    while n < (1 << 8):
        n *= b
    assert is_sorta_square_free(lambda: pn_d01(b), b, n)


@mark.parametrize("b", range(2, 1025))
def test_overlap_free(b: int):
    n = b
    while n < (1 << 8):
        n *= b
    assert is_overlap_free(lambda: pn_d01(b), b, n)


@mark.parametrize("b", range(2, 1025))
def test_cube_free(b: int):
    n = b
    while n < (1 << 8):
        n *= b
    assert is_cube_free(lambda: pn_d01(b), b, n)
