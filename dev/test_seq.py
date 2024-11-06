from importlib import import_module
from itertools import product
from pathlib import Path
from signal import SIGTERM, signal
from typing import Dict, Iterable

from pytest import mark

test_len = 2**15
bases_tested = range(2, 256)
base_2_tests = [int(p.name[1:-3]) for p in Path(__file__).parent.glob('p2/d*.py')]
base_n_tests = [int(p.name[1:-3]) for p in Path(__file__).parent.glob('pn/d*.py')]
base_2_tests.remove(1)
base_n_tests.remove(1)


def signal_handler(sig, frame):
    print("Received SIGTERM. Raising exception for pytest.")
    raise RuntimeError()


signal(SIGTERM, signal_handler)


def get_iters(p2: bool = True, pn: bool = False, s: int = 2) -> Dict[str, Iterable[int]]:
    parent_name = '.'.join(__name__.split('.')[:-1])
    iters = {}
    for kind in "2" * p2 + "n" * pn:
        for d in range(1, 100):
            name = f'p{kind}.d{d:02}'
            try:
                iters[name] = getattr(import_module(f'{parent_name}.{name}'), f'{name.replace(".", "_")}')(s)
            except ImportError:
                continue
            except Exception as e:
                print(e)
    return iters


@mark.parametrize("c", [f'2_{n:02}' for n in base_2_tests] + ['n_01'] + [f'n_{n:02}' for n in base_n_tests])
def test_compare_2_1_to_(c: str, n: int = test_len):
    iters = get_iters(True, True)
    cs = 'p{}.d{}'.format(*c.split('_'))
    iters = {
        k: d for k, d in iters.items()
        if k in (cs, "p2.d01")
    }
    assert len(iters) == 2
    for idx, tup in enumerate(zip(*iters.values())):
        if len(set(tup)) != 1:
            raise ValueError(f"Failed at idx {idx}: {dict((f, x) for f, x in zip(iters.keys(), tup))}")
        if idx >= n:
            break
    print(f"All definitions agree for 2 players up to {n} iterations")


@mark.parametrize("s, c", product(bases_tested, base_n_tests),
                  ids=(f'{c:01}-base_{s:03}' for s, c in product(bases_tested, base_n_tests)))
def test_compare_n_1_to_n(c: int, s: int, n: int = test_len):
    iters = get_iters(False, True, s)
    cs = str(c).zfill(2)
    iters = {
        k: d for k, d in iters.items()
        if cs in k or "01" in k
    }
    assert len(iters) == 2
    for idx, tup in enumerate(zip(*iters.values())):
        if len(set(tup)) != 1:
            raise ValueError(f"Failed at idx {idx}: {dict((f, x) for f, x in zip(iters.keys(), tup))}")
        if idx >= n:
            break
    print(f"All definitions agree for {s} players up to {n} iterations")
