class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp where dp[a] = min coins needed to make amount a
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        return -1 if dp[amount] == float('inf') else dp[amount]
        