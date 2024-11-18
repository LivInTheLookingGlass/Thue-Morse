try:
    from bitarray import *  # noqa: F401, F403
except (ImportError, ModuleNotFoundError):
    from warnings import warn

    warn("Unable to load the bitarray library. Doing our best to substitute", category=ImportWarning)

    class bitarray(bytearray):  # type: ignore
        def invert(self):
            for i in range(len(self)):
                self[i] = not self[i]

        def copy(self) -> 'bitarray':  # type: ignore
            return bitarray(self)
