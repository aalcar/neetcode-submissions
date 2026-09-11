from functools import cache


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for l in range(n - 2, 0, -1):
            for r in range(l, n - 1):
                for i in range(l, r + 1):
                    coins = nums[l - 1] * nums[i] * nums[r + 1]
                    coins += dp[l][i - 1] + dp[i + 1][r]

                    dp[l][r] = max(dp[l][r], coins)

        return dp[1][n - 2]
