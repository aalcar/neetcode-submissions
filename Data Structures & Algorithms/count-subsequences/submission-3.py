from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        subsequence:
        pick or dont pick letters
        has to be in original order
        dp(i, j) -> number of distinct subsequences
        i -> index in s str
        j -> index in t str
        rr:
        dp(i, j)
        res = dp(i + 1, j)
        if s[i] == s[j]:
            res += dp(i + 1, j + 1)
        
        base cases:
        if i == len(s):
            return 0
        if j == len(t):
            return 1
        """
        dp = [[-1] * len(t) for _ in range(len(s))]
        def dfs(i, j):
            if j == len(t):
                return 1

            if i == len(s):
                return 0
 
            if dp[i][j] != -1:
                return dp[i][j]

            res = dfs(i + 1, j)
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            
            dp[i][j] = res
            return res

        return dfs(0, 0)