try:
    from numba import *  # noqa: F401, F403
except (ImportError, ModuleNotFoundError):
    from warnings import warn

    from .fluidpythran import boost

    warn("Unable to load the numba library. Doing our best to substitute", category=ImportWarning)

    def jit(x=None, **kwargs):
        if x:
            return boost(x)
        return lambda a: boost(a)
