class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        half = sum(nums) // 2

        # dp[i] = can we form sum i using a subset of the numbers so far
        dp = [False] * (half + 1)

        dp[0] = True
        for num in nums:
            for i in range(half, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[half]
