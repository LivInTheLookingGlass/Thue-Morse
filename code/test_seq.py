from importlib import import_module
from typing import Dict, Iterable

from pytest import mark

test_len = 2**10


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


@mark.parametrize("c", range(2, 11))
def test_2(c: int, n: int = test_len):
    iters = get_iters(True, True)
    cs = str(c).zfill(2)
    iters = {
        k: d for k, d in iters.items()
        if cs in k or "01" in k
    }
    for idx, tup in enumerate(zip(*iters.values())):
        if len(set(tup)) != 1:
            raise ValueError(f"Failed at idx {idx}: {dict((f, x) for f, x in zip(iters.keys(), tup))}")
        if idx >= n:
            break
    print(f"All definitions agree for 2 players up to {n} iterations")


@mark.parametrize("s", range(3, 33))
def test_n(s: int, n: int = test_len):
    iters = get_iters(False, True, s)
    sn = s * n
    for idx, tup in enumerate(zip(*iters.values())):
        if len(set(tup)) != 1:
            raise ValueError(f"Failed at idx {idx}: {dict((f, x) for f, x in zip(iters.keys(), tup))}")
        if idx >= sn:
            break
    print(f"All definitions agree for {s} players up to {n} iterations")
