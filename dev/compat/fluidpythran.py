try:
    from fluidpython import *  # noqa: F401, F403
except (ImportError, ModuleNotFoundError):
    from warnings import warn

    warn("Unable to load the fluidpythran library. Doing our best to substitute", category=ImportWarning)

    def boost(x=None, **kwargs):
        if x:
            return x
        return lambda a: a
