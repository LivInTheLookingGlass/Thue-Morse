try:
    from gmpy2 import *
except ImportError:
    from warnings import ImportWarning, warn

    warn("Unable to load the gmpy2 library. Doing our best to substitute", category=ImportWarning)

    mpz = int
