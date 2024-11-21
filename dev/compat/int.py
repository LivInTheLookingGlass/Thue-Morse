if hasattr(int, 'bit_count'):
    bit_count = int.bit_count

else:
    def bit_count(x: int) -> int:
        return bin(x).count('1')
