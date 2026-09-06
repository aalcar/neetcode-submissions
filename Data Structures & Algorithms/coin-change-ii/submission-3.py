class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dfs(curr, i) -> number of paths formed to amt
        # rr: dfs(curr - coins[i], i) + dfs(curr, i + 1)
        # base: curr == 0, +1, i >= len, +0
        coins.sort()
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        # you need 0 coins to make amt 0
        for i in range(len(coins) + 1):
            dp[i][0] = 1
        
        for i in range(len(coins) - 1, -1, -1):
            for curr in range(coins[i], amount + 1):
                dp[i][curr] = dp[i + 1][curr] + dp[i][curr - coins[i]]

        return dp[0][amount]