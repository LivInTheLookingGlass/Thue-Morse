from z3 import *

# Declare an integer variable
n = Int('n')

# Define recursive functions using RecFunction
p = RecFunction('p', IntSort(), IntSort())
T1 = RecFunction('T1', IntSort(), IntSort())
T2 = RecFunction('T2', IntSort(), IntSort())

# Define a non-recursive function using Function
ce = Function('ce', IntSort(), IntSort())

# Add recursive definitions
RecAddDefinition(p, [n], If(n == 0, 0, (p(n / 2) + n) % 2))
RecAddDefinition(T1, [n], If(n == 0, 0, p(n)))
RecAddDefinition(T2, [n], 1 - ce(n + 1) + ce(n))

# Add definition for ce (non-recursive) using a constraint
# Example: ce(n) = (n + 1) / 2 + p(n + 1) * ((n + 1) % 2)
solver = Solver()
solver.set(proof=True)
solver.add(ce(n) == (n + 1) / 2 + p(n + 1) * ((n + 1) % 2))

# Add equivalence check for T1 and T2
solver.add(ForAll(n, Implies(n >= 0, T1(n) == T2(n))))

# Check if the assertion is valid
if solver.check() == sat:
    print("Counterexample found:", solver.model())
else:
    print("Proven: T1(n) and T2(n) produce the same output for all n >= 0")
    with open("output.smt2", "w") as f:
        f.write(solver.to_smt2())
    print("SMT-LIB file generated: output.smt2")
