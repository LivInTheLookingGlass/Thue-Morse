from importlib import import_module
from itertools import combinations, product
from pathlib import Path
from signal import SIGTERM, signal
from typing import Dict, Iterable

from pytest import mark
try:
    from z3 import *
    disable_z3 = False
except ImportError:
    disable_z3 = True

from . import get_iters, get_z3s

test_len = 2**15
bases_tested = range(2, 256)
base_2_tests = [int(p.name[1:-3]) for p in Path(__file__).parent.glob('p2/d*.py')]
base_n_tests = [int(p.name[1:-3]) for p in Path(__file__).parent.glob('pn/d*.py')]
base_2_tests.remove(1)
base_n_tests.remove(1)
z3_tests = [x + y for x, y in combinations(get_z3s(True, True).items(), 2)]


def signal_handler(sig, frame):
    print("Received SIGTERM. Raising exception for pytest.")
    raise RuntimeError()


signal(SIGTERM, signal_handler)


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


@mark.skipif(disable_z3, reason="Requires z3-solver")
@mark.parametrize("T1_name, T1, T2_name, T2", z3_tests,
                  ids=(f'{T1_name}-vs-{T2_name}' for T1_name, _, T2_name, _ in z3_tests))
def test_z3_cmp(T1_name: str, T1, T2_name, T2):
    solver = Solver()
    solver.set(proof=True)

    # Add equivalence check for T1 and T2
    solver.add(ForAll(n, Implies(n >= 0, T1(n) == T2(n))))

    # Check if the assertion is valid
    if solver.check() == sat:
        raise ValueError("Counterexample found:", solver.model())
    print("Proven: T1(n) and T2(n) produce the same output for all n >= 0")
    fname = f"{T1_name.replace('.', '_')}_vs_{T2_name.replace('.', '_')}.smt2"
    with open(fname, "w") as f:
        f.write(solver.to_smt2())
    print("SMT-LIB file generated:", fname)
    print("Trying proof...")
    try:
        print(solver.proof())
    except Exception:
        print("Proof failed. Moving on.")
