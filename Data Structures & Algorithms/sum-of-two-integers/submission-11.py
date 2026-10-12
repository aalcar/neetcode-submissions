class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        use bitwise ops
        0100
        0111
        ----
        1011

        use AND to find carry
        use XOR to find digit placed in
        """

        res = 0
        carry = 0
        mask = (1 << 32) - 1

        # Flipping bits to 1 in res. Iterating right to left
        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1

            digit = a_bit ^ b_bit ^ carry
            carry = (a_bit & b_bit) | (a_bit & carry) | (b_bit & carry)

            res |= (digit << i)

        if res > (1 << 31):
            res = ~(res ^ mask)

        return res
