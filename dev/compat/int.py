if hasattr(int, 'bit_count'):
    bit_count = int.bit_count

else:
    def bit_count(self: int) -> int:
        return bin(self).count('1')
