from functools import partial
from itertools import combinations, product
from pathlib import Path
from signal import SIGTERM, signal
from typing import Any, List, Literal, Union

from pytest import mark

try:
    from z3 import And, ForAll, Implies, Int, OnClause, RecFunction, Solver, sat, set_param
    disable_z3 = False
    set_param('verbose', 1)
    for param in ('stats', 'proof', 'model', 'dump_models', 'unsat_core'):
        set_param(param, True)
except ImportError:
    Int = str  # type: ignore
    disable_z3 = True

from . import get_iters, get_z3s

s_ref = Int('s')
test_len = 2**15
bases_tested = range(2, 256)
base_2_tests = [int(p.name[1:-3]) for p in Path(__file__).parent.glob('p2/d*.py')]
base_n_tests = [int(p.name[1:-3]) for p in Path(__file__).parent.glob('pn/d*.py')]
base_2_tests.remove(1)
base_n_tests.remove(1)
z3_tests_b2 = [x + y for x, y in combinations(get_z3s(True, True).items(), 2)]
z3_tests_bn = [x + y for x, y in combinations(get_z3s(False, True, s_ref).items(), 2)]


@partial(signal, SIGTERM)
def signal_handler(sig, frame):
    print("Received SIGTERM. Raising exception for pytest.")
    raise RuntimeError()


@mark.skipif(disable_z3, reason="Requires z3-solver")
@mark.parametrize("T1_name, T1, T2_name, T2", z3_tests_b2,
                  ids=(f'{T1_name}-vs-{T2_name}' for T1_name, _, T2_name, _ in z3_tests_b2))
def test_z3_cmp_b2(T1_name: str, T1: 'RecFunction', T2_name, T2: 'RecFunction'):
    run_solver(T1_name, T1, T2_name, T2, "2", [])


@mark.skipif(disable_z3, reason="Requires z3-solver")
@mark.parametrize("T1_name, T1, T2_name, T2", z3_tests_bn,
                  ids=(f'{T1_name}-vs-{T2_name}' for T1_name, _, T2_name, _ in z3_tests_bn))
def test_z3_cmp_bn(T1_name: str, T1: 'RecFunction', T2_name, T2: 'RecFunction'):
    run_solver(T1_name, T1, T2_name, T2, "n", [s_ref >= 2])


def run_solver(
    T1_name: str, T1: 'RecFunction',
    T2_name: str, T2: 'RecFunction',
    mode: Union[Literal["2"], Literal["n"]],
    extras: List[Any]
) -> None:
    solver = Solver()
    solver.reset()
    solver.set("cache_all", True)
    solver.set("clause_proof", True)
    OnClause(solver, lambda pr, clause: ...)  # for some reason, eliminating this line means no proofs are printed

    n = Int('n')
    solver.add(*extras)
    solver.add(ForAll(n, Implies(And(n >= 0, n < s_ref), And(T1(n) == n, T2(n) == n))))
    solver.add(T1(s_ref) == 1, T2(s_ref) == 1)
    solver.add(ForAll(n, Implies(n >= 0, T1(n) == T2(n))))

    # Check if the assertion is valid
    if solver.check() == sat:
        raise ValueError("Counterexample found:", solver.model())
    print(f"Proven: {T1_name}(n, s) and {T2_name}(n, s) produce the same output for all n >= 0, s >= 2")

    print("Statistics:")
    print(solver.statistics())

    fname_noext = f"{T1_name.replace('.', '_')}-vs-{T2_name.replace('.', '_')}"
    fname = Path(f"./prover/smt/p{mode}/{fname_noext}.smt2")
    fname.parent.mkdir(exist_ok=True, parents=True)
    with fname.open("w") as f:
        f.write(solver.to_smt2())
    print("SMT-LIB file generated:", fname)

    print("Trying model...")
    try:
        m = solver.model()
        print("Traversing model...")
        fname = Path(f"./prover/model/p{mode}/{fname_noext}.smt2")
        fname.parent.mkdir(exist_ok=True, parents=True)
        with fname.open("w") as f:
            for d in m.decls():
                string = f'{d.name()} = {m[d]}'
                print(string)
                f.write(string)
    except Exception:
        print("Model failed. Moving on.")

    print("Trying proof...")
    try:
        print(solver.proof())
        fname = Path(f"./prover/proof/p{mode}/{fname_noext}.smt2")
        fname.parent.mkdir(exist_ok=True, parents=True)
        with fname.open("w") as f:
            f.write(str(solver.proof()))
    except Exception:
        print("Proof failed. Moving on.")


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
