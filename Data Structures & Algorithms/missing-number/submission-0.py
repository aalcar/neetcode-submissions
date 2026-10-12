class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        n XOR n = 0
        n XOR 0 = n
        """
        res = len(nums)
        for i in range(len(nums)):
            res ^= nums[i] ^ i

        return res