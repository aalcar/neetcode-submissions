class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # can buy on i and choose again at i + 2
        # can skip on i and choose at i + 1
        # dp(index, stock_held) = max profit
        """
        1 -> buy 1 or dont buy 1
        move onto 3 where i could sell or skip OR buy or skip
        max(sell, skip) OR max(buy, skip)
        ie. max(dp(i + 1, -1) + stock_held, dp(i + 1, stock_held)) 
        or
            max(dp(i + 2, s[i]), dp(i + 1, stock_held))
        """
        dp = defaultdict(int)
        def dfs(i, stock_held):
            if i >= len(prices):
                return 0

            if (i, stock_held) in dp:
                return dp[(i, stock_held)]

            # buying
            if stock_held == -1:
                dp[(i, stock_held)] = max(dfs(i + 1, prices[i]) - prices[i], dfs(i + 1, stock_held))
            # selling
            else:
                dp[(i, stock_held)] = max(dfs(i + 2, -1) + prices[i], dfs(i + 1, stock_held))
            
            return dp[(i, stock_held)]

        return dfs(0, -1)