try:
    from bitarray import *
except ImportError:
    class bitarray(bytearray):
        def invert(self):
            for i in range(len(self)):
                self[i] = not self[i]

        def copy(self) -> 'bitarray':
            return bitarray(self)
