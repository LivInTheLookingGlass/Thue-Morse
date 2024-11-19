from importlib import import_module
from traceback import print_exc
from types import ModuleType
from typing import Any, Callable, Dict, Generator, Sequence

parent_name = '.'.join(__name__.split('.')[:-1])


def get_modules(p2: bool = True, pn: bool = False, s: int = 2) -> Dict[str, ModuleType]:
    iters = {}
    for kind in "2" * p2 + "n" * pn:
        for d in range(1, 100):
            name = f'p{kind}.d{d:02}'
            try:
                iters[name] = import_module(f'{parent_name}.{name}', __name__)
            except ImportError:
                continue
    return iters


def get_iters(*names: str) -> Sequence[Callable[[int], Generator[int, None, None]]]:
    return [
        getattr(
            import_module(f'{parent_name}.{key}', __name__),
            f'{key.replace(".", "_")}'
        )
        for key in names
    ]


def get_z3s(p2: bool = True, pn: bool = False, s: int = 2) -> Dict[str, Dict[str, Any]]:
    ret: Dict[str, Dict[str, Any]] = {}
    for key, value in get_modules(True, True).items():
        if hasattr(value, 'to_z3') and (('p2' in key and p2) or ('pn' in key and pn)):
            try:
                ret[key] = value.to_z3(s)
            except Exception:
                print_exc()
    return ret
