class Solution:
    def reverseBits(self, n: int) -> int:
        num = 0
        for i in range(32):
            if n & (1 << i):
                num = 2 * num + 1
            else:
                num = 2 * num 

        return num