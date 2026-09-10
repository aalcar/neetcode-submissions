from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        my logic:
        go path of least resistance to minimize
        if equal: move i and j
        -- keys, ley
        good case: dp(i + 1, j + 1)
        insert: dp(i, j + 1) + 1
        delete: dp(i + 1, j) + 1
        replace: dp(i + 1, j + 1) + 1

        bottom up
           m  o  n  e  y
        m -1 -1 -1 -1 -1  7
        o -1 -1 -1 -1 -1  6
        n -1 -1 -1 -1 -1  5
        k -1 -1 -1 -1 -1  4
        e -1 -1 -1 -1 -1  3
        y -1 -1 -1 -1 -1  2
        s -1 -1 -1 -1 -1  1
           5  4  3  2  1  0
        """
        n, m = len(word1), len(word2)
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][m] = n - i
        
        for j in range(m + 1):
            dp[n][j] = m - j

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j + 1], dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]
