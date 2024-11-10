from itertools import combinations, repeat

from z3 import *

from dev import get_z3

for (T1_name, T1), (T2_name, T2) in combinations(get_z3s(),items(), 2):
    solver = Solver()
    solver.set(proof=True)

    # Add equivalence check for T1 and T2
    solver.add(ForAll(n, Implies(n >= 0, T1(n) == T2(n))))

    # Check if the assertion is valid
    if solver.check() == sat:
        print("Counterexample found:", solver.model())
        continue
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
    print()
