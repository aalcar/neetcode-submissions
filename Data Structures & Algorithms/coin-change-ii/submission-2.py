class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # adding all different paths
        # dfs(curr, i),  number of paths formed to amt
        # you could add however you many coins you want from i
        # then move onto next i
        dp = defaultdict(int)
        def dfs(curr, i):
            if (curr, i) in dp:
                return dp[(curr, i)]

            if curr == 0:
                return 1

            if i >= len(coins):
                return 0
            
            total = 0
            if curr >= 0:
                total += dfs(curr, i + 1) + dfs(curr - coins[i], i)

            dp[(curr, i)] = total
            return total
        
        return dfs(amount, 0)