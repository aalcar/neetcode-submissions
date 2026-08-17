class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def dfs(curr):
            if curr >= n:
                return curr == n
            
            if cache[curr] != -1:
                return cache[curr]

            count = dfs(curr + 1) + dfs(curr + 2)

            cache[curr] = count 
            return count

        return dfs(0)