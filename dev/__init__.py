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


def get_modules(p2: bool = True, pn: bool = False, s: int = 2) -> Dict[str, Iterable[int]]:
    parent_name = '.'.join(__name__.split('.')[:-1])
    iters = {}
    for kind in "2" * p2 + "n" * pn:
        for d in range(1, 100):
            name = f'p{kind}.d{d:02}'
            try:
                iters[name] = import_module(f'{parent_name}.{name}', __name__)
            except ImportError:
                continue
            except Exception as e:
                print(e)
    return iters


def get_iters(p2: bool = True, pn: bool = False, s: int = 2) -> Dict[str, Iterable[int]]:
    return {
        key: getattr(val, f'{key.replace(".", "_")}')(s)
        for key, value in get_modules().items()
        if ('p2' in key and p2) or ('pn' in key and pn)
    }


def get_z3s(p2: bool = True, pn: bool = False, s: int = 2) -> Dict[str, Iterable[int]]:
    return {
        key: val.get_z3(s)
        for key, value in get_modules().items()
        if hasattr(value, 'get_z3') and (('p2' in key and p2) or ('pn' in key and pn))
    }
