try:
    from fluidpython import *
except ImportError:
    from warnings import ImportWarning, warn

    warn("Unable to load the fluidpythran library. Doing our best to substitute", category=ImportWarning)


    def boost(x = None, **kwargs):
        if x:
            return x
        return lambda a: a
