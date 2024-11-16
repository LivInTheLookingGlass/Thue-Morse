try:
    from fluidpython import *
except ImportError:
    def boost(x = None, **kwargs):
        if x:
            return x
        return lambda a: a
