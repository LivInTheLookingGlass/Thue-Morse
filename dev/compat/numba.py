try:
    from numba import *
except ImportError:
    def jit(x = None, **kwargs):
        if x:
            return x
        return lambda a: a
