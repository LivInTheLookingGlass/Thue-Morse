from functools import partial
from itertools import combinations, islice, product
from pathlib import Path
from signal import SIGTERM, signal
from typing import Any, List, Literal, Set, Tuple, Union

from pytest import mark, skip, xfail

from . import get_iters, get_z3s
from .compat.fluidpythran import boost
from .compat.z3 import And, Exists, ForAll, Implies, Int, OnClause, RecFunction, Solver, Z3Exception, disable_z3, z3
from .p2.d15 import ensure_pool

ensure_pool()

s_ref = Int('s')
test_len = 2**15
bases_tested = range(2, 256)
base_2_tests = [int(p.name[1:-3]) for p in Path(__file__).parent.glob('p2/d*.py')]
base_n_tests = [int(p.name[1:-3]) for p in Path(__file__).parent.glob('pn/d*.py')]
base_2_tests.remove(1)
base_n_tests.remove(1)

already_proven_b2 = {
    ('p2.d01', 'p2.d02'),
    ('p2.d01', 'p2.d03'),
    ('p2.d01', 'p2.d06'),
    ('p2.d04', 'pn.d08'),
    ('p2.d15', 'pn.d09'),
} | {
    (f'p2.d{n:02}', f'pn.d{n:02}') for n in range(1, 8)
}

already_proven_bn = {
    ('pn.d01', 'pn.d02'),
    ('pn.d03', 'pn.d08'),
}


def make_set_commutative(s: Set[Tuple[str, str]]):
    length = 0
    while length != len(s):
        to_add = set()
        for (x, y), (w, z) in product(s, repeat=2):
            if x == w and y != z:
                to_add.add((y, z))
            if x == z and y != w:
                to_add.add((y, w))
            if y == w and x != z:
                to_add.add((x, z))
            if y == z and x != w:
                to_add.add((x, w))
        length = len(s)
        s.update(to_add)


make_set_commutative(already_proven_b2)
make_set_commutative(already_proven_bn)
z3_tests_b2 = [
    x + y
    for x, y in combinations(get_z3s(True, True).items(), 2)
    if (x[0], y[0]) not in already_proven_b2
]
z3_tests_bn = [
    x + y
    for x, y in combinations(get_z3s(False, True, s_ref).items(), 2)
    if (x[0], y[0]) not in already_proven_bn
]


@partial(signal, SIGTERM)
def signal_handler(*args, **kwargs):
    print("Received SIGTERM. Raising exception for pytest.")
    raise RuntimeError()


@mark.parametrize("n", [1 << x for x in range(4, 8)])
@mark.parametrize("c", ['2_01'] + [f'2_{n:02}' for n in base_2_tests] + ['n_01'] + [f'n_{n:02}' for n in base_n_tests])
@boost
def test_benchmark(benchmark, c: str, n: int):
    cs = 'p{}.d{}'.format(*c.split('_'))
    iterator = get_iters(cs)[0]

    def to_check():
        it = iterator(2, n)
        result = []
        try:
            for i in islice(it, n):
                result.append(i)
        except RuntimeError:
            pass
        finally:
            it.close()
        return result

    results = benchmark(to_check)
    comparison = "p2.d01" if cs != "p2.d01" else "p2.d02"
    iterator = get_iters(comparison)[0]
    for idx, (x, y) in enumerate(zip(results, iterator(2))):
        if x != y:
            raise ValueError(f"At T({idx}), {cs} diverges from {comparison}: {x} != {y}")


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
    solver.set("cache_all", True)
    solver.set("clause_proof", True)
    OnClause(solver, lambda pr, clause: ...)  # for some reason, eliminating this line means no proofs are printed

    fname_noext = f"{T1_name.replace('.', '_')}-vs-{T2_name.replace('.', '_')}"
    fname = Path(f"./prover/smt/p{mode}/{fname_noext}.smt2")

    n = Int('n')
    standard_asserts = [
        *extras,
        ForAll(n, Implies(And(n >= 0, n < s_ref), And(T1(n) == n, T2(n) == n))),
        T1(s_ref) == 1, T2(s_ref) == 1,
    ]
    solver.add(*standard_asserts)
    solver.push()
    solver.add(Exists(n, And(n >= 0, T1(n) != T2(n))))

    try:
        checkpoint = solver.check()
    except (Z3Exception, MemoryError) as e:
        xfail(reason=repr(e))

    match checkpoint:
        case z3.sat:
            print("Counterexample found!")
            dump_solver(fname, fname_noext, mode, solver)
            raise ValueError("Counterexample found!")
        case z3.unknown:
            print("Unable to find or disprove a counterexample")
        case z3.unsat:
            pass
        case _:
            raise RuntimeError("Unknown status: ", checkpoint)
    print("Refutation Phase Statistics:")
    print(solver.statistics())
    print("Counterexample not found. Trying for proof of equality...")

    solver.pop()
    # solver.add(*standard_asserts)
    solver.add(ForAll(n, Implies(n >= 0, T1(n) == T2(n))))

    try:
        checkpoint = solver.check()
    except (Z3Exception, MemoryError) as e:
        xfail(reason=repr(e))
    match checkpoint:
        case z3.unsat:
            raise ValueError("Proof failed:", solver.unsat_core(), solver.model())
        case z3.unknown:
            skip("Wasn't able to figure out a solution")
        case z3.sat:
            pass
        case _:
            raise RuntimeError("Unknown status: ", checkpoint)
    print(f"Proven: {T1_name}(n, s) and {T2_name}(n, s) produce the same output for all n >= 0, s >= 2")

    print("Statistics:")
    print(solver.statistics())
    dump_solver(fname, fname_noext, mode, solver)


def dump_solver(fname: Path, fname_noext: str, mode: str, solver: 'Solver') -> None:
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
@boost
def test_compare_2_1_to_(c: str, n: int = test_len):
    cs = 'p{}.d{}'.format(*c.split('_'))
    iters = get_iters("p2.d01", cs)
    assert len(iters) == 2
    iterators = [iterator(2, n) for iterator in iters]
    try:
        for idx, tup in enumerate(zip(*iterators)):
            if len(set(tup)) != 1:
                raise ValueError(f"Failed at idx {idx}: {dict((repr(f), x) for f, x in zip(iters, tup))}")
            if idx >= n:
                break
    except RuntimeError:
        pass  # sympy loses precision compared to mathematica on some sequences
    print(f"All definitions agree for 2 players up to {n} iterations")
    for it in iterators:
        it.close()


@mark.parametrize("s, c", product(bases_tested, base_n_tests),
                  ids=(f'{c:01}-base_{s:03}' for s, c in product(bases_tested, base_n_tests)))
@boost
def test_compare_n_1_to_n(c: int, s: int, n: int = test_len):
    cs = f"pn.d{c:02}"
    iters = get_iters("pn.d01", cs)
    assert len(iters) == 2
    iterators = [iterator(s) for iterator in iters]
    for idx, tup in enumerate(zip(*iterators)):
        if len(set(tup)) != 1:
            raise ValueError(f"Failed at idx {idx}: {dict((repr(f), x) for f, x in zip(iters, tup))}")
        if idx >= n:
            break
    print(f"All definitions agree for {s} players up to {n} iterations")
    for it in iterators:
        it.close()
