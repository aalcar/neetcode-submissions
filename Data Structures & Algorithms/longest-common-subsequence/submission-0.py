class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 1. function -- solve a state
        # 2. recursive relation -- transition between states
        # 3. base cases

        n, m = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # fill in reverse like you would with dfs
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]