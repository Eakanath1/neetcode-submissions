class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask and max positive int
        mask    = (1 << 32) - 1     # 0xFFFFFFFF
        MAX_INT = (1 << 31) - 1     # 0x7FFFFFFF

        # Iterate until no carry remains
        while b != 0:
            # compute carry & partial sum, then mask down to 32 bits
            carry = (a & b) & mask
            a     = (a ^ b) & mask
            b     = (carry << 1) & mask

        # if a is in [0..MAX_INT], it's a valid positive result
        if a <= MAX_INT:
            return a
        # else a represents a negative number in two's-complement
        return ~(a ^ mask)