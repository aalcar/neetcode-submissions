class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # track the minValue and see if the profit from selling at prices[i]
        # is better than your max
        maxProfit = 0
        minValue = float('inf')
        for price in prices:
            minValue = min(minValue, price)
            maxProfit = max(maxProfit, price - minValue)

        return maxProfit
        