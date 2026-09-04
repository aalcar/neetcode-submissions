class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        0 1 1  1   1    1
        1 2 3  4   5   6
        1 3 6 10 15 21

        0 1 1
        1 2 3
        1 3 6
        
        initialize m * n table
        make start 0 and borders 1
        starting at 1,1? what about 1x1 1x2 or 2x1?
        iterate until you dont find a used one? but like why
        """
        if m == 1 and n == 1:
            return 1

        if (m == 1 and n == 2) or (m == 2 and n == 1):
            return 1
        
        dp = [[1] * n for _ in range(m)] 
        dp[0][0] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]