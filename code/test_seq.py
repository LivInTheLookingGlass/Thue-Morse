from importlib import import_module
from typing import Dict, Iterable

from pytest import mark

test_len = 2**15


def get_iters(p2: bool = True, pn: bool = False, s: int = 2) -> Dict[str, Iterable[int]]:
    parent_name = '.'.join(__name__.split('.')[:-1])
    iters = {}
    for kind in "2" * p2 + "n" * pn:
        for d in range(1, 100):
            name = f'p{kind}_d{d:02}'
            try:
                iters[name] = getattr(import_module(f'{parent_name}.{name}'), f'seq_{name}')(s)
            except ImportError:
                continue
            except Exception as e:
                print(e)
    return iters


def test_2(n: int = test_len):
    iters = get_iters(True, True)
    for idx, tup in enumerate(zip(*iters.values())):
        if len(set(tup)) != 1:
            raise ValueError(f"Failed at idx {idx}: {dict((f, x) for f, x in zip(iters.keys(), tup))}")
        if idx >= n:
            break
    print(f"All definitions agree for 2 players up to {n} iterations")


@mark.parametrize("s", range(2, 33))
def test_n(s: int, n: int = test_len // 2):
    iters = get_iters(False, True, s)
    sn = s * n
    for idx, tup in enumerate(zip(*iters.values())):
        if len(set(tup)) != 1:
            raise ValueError(f"Failed at idx {idx}: {dict((f, x) for f, x in zip(iters.keys(), tup))}")
        if idx >= sn:
            break
    print(f"All definitions agree for {s} players up to {n} iterations")
