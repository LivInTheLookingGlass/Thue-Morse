from importlib import import_module
from typing import Dict, Iterable


def get_iters(p2: bool = True, pn: bool = False, s: int = 2) -> Dict[str, Iterable[int]]:
    parent_name = '.'.join(__name__.split('.')[:-1])
    iters = {}
    for kind in "2" * p2 + "n" * pn:
        for d in range(1, 10):
            name = f'p{kind}_d{d}'
            try:
                iters[name] = getattr(import_module(f'{parent_name}.{name}'), f'seq_{name}')(s)
            except Exception as e:
                print(e)
    return iters


def test_2(n: int = 2**10):
    iters = get_iters(True, True)
    for idx, tup in enumerate(zip(*iters.values())):
        if len(set(tup)) != 1:
            raise ValueError(f"Failed at idx {idx}: {dict((f, x) for f, x in zip(iters.keys(), tup))}")
        if idx >= n:
            break
    print(f"All definitions agree for 2 players up to {n} iterations")


def test_n(n: int = 2**9):
    for s in range(2, 17):
        iters = get_iters(False, True, s)
        sn = s * n
        for idx, tup in enumerate(zip(*iters.values())):
            if len(set(tup)) != 1:
                raise ValueError(f"Failed at idx {idx}: {dict((f, x) for f, x in zip(iters.keys(), tup))}")
            if idx >= sn:
                break
        print(f"All definitions agree for {s} players up to {n} iterations")
