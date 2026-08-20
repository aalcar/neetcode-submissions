class Solution:
    def countSubstrings(self, s: str) -> int:
        # re-use palindrome dp sol for O(1) checks
        # can find all palindromes in O(n^2)
        res = 0
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    res += 1

        return res