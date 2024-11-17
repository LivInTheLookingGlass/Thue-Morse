try:
    import z3  # noqa: F401, F403
    # because we need to use names like z3.sat for match statements
    from z3 import (And, Exists, ForAll, Implies, Int, OnClause, RecFunction, Solver, Z3Exception,  # noqa: F401, F403
                    set_param)

    disable_z3 = False
    set_param('verbose', 1)
    for param in ('stats', 'proof', 'model', 'dump_models', 'unsat_core'):
        set_param(param, True)
except (ImportError, ModuleNotFoundError):
    from sys import modules
    from warnings import warn

    warn("Umable to load the z3 module. Providing dummy objects", category=ImportWarning)

    Int = str  # type: ignore
    disable_z3 = True
    current_module = modules[__name__]
    for name in (
        'And', 'Exists', 'ForAll', 'Implies', 'OnClause', 'RecFunction', 'Solver', 'Z3Exception',
        'set_param', 'z3'
    ):
        setattr(current_module, name, None)
