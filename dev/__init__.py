from importlib import import_module
from traceback import print_exc
from types import ModuleType
from typing import Dict, Iterable

try:
    from z3 import RecFunction
except ImportError:
    pass


def get_modules(p2: bool = True, pn: bool = False, s: int = 2) -> Dict[str, ModuleType]:
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
        key: getattr(value, f'{key.replace(".", "_")}')(s)
        for key, value in get_modules(p2, pn).items()
        if ('p2' in key and p2) or ('pn' in key and pn)
    }


def get_z3s(p2: bool = True, pn: bool = False, s: int = 2) -> Dict[str, Dict[str, 'RecFunction']]:
    ret: Dict[str, Dict[str, 'RecFunction']] = {}
    for key, value in get_modules(p2, pn).items():
        if hasattr(value, 'to_z3') and (('p2' in key and p2) or ('pn' in key and pn)):
            try:
                ret[key] = value.to_z3(s)
            except Exception:
                print_exc()
    return ret
