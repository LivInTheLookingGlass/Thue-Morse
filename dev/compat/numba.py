try:
    from numba import *
except ImportError:
    from warnings import ImportWarning, warn

    warn("Unable to load the numba library. Doing our best to substitute", category=ImportWarning)


    def jit(x = None, **kwargs):
        if x:
            return x
        return lambda a: a
