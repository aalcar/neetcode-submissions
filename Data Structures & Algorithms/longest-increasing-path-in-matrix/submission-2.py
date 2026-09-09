class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # go through each cell and find its longest increasing path
        """
        fnc: dp(i, j) = length of longest increasing path
        rr: max(dp(i + 1, j), dp(i - 1, j), dp(i, j + 1), dp(i, j - 1))
        -- not this simple, we need to only traverse spots where its bigger and add 1
        for dx, dy in directions:
            maxLength = max(maxLength, dp(i + dx, j + dy))
        return 1 + maxLength
        bc: if out of bounds, return 0
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def outOfBounds(i, j):
            return (min(i, j) < 0 or 
                i >= len(matrix) or
                j >= len(matrix[0]))

        n, m = len(matrix), len(matrix[0])
        dp = defaultdict(int)
        def dfs(i, j):
            if outOfBounds(i, j):
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]

            length = 0
            for dx, dy in directions:
                k, l = i + dx, j + dy
                if outOfBounds(k, l) or matrix[i][j] < matrix[k][l]:
                    dp[(k, l)] = dfs(k, l)
                    length = max(length, dp[(k, l)])
            
            return 1 + length

        length = 0
        for i in range(n):
            for j in range(m):
                length = max(length, dfs(i, j))

        return length