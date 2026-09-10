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
        n, m = len(s), len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][m] = 1

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]

                print(dp[i][j])

        return dp[0][0]