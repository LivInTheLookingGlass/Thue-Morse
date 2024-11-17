try:
    from gmpy2 import *  # noqa: F401, F403
except (ImportError, ModuleNotFoundError):
    from warnings import warn

    warn("Unable to load the gmpy2 library. Doing our best to substitute", category=ImportWarning)

    mpz = int
