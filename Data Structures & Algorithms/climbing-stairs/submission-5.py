class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        # 1 moves you 1
        # 2 moves you 2
        # 1 + 1 moves you the same as two
        # 
        # 7
        cache = [-1] * n
        def backtrack(curr):
            if curr == n:
                return 1

            if curr > n:
                return 0

            if cache[curr] != -1:
                return cache[curr]

            count = backtrack(curr + 1) + backtrack(curr + 2)

            cache[curr] = count 
            return count

        backtrack(0)
        return cache[0]