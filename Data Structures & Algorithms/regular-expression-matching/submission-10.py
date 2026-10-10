from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        fn(i, j) -> bool
        rr: if next is *, ret if (i + 1, j){if length permits} or (i, j+2) is good
        if next is not *, check if match, no match is false, match is (i + 1, j + 1)
        base cases: end of s and p reached -> true, end of p but not s -> false
        """
        n, m = len(s), len(p)
        cache = defaultdict(int)
        def dp(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if j == m:
                return i == n
            
            char_match = i < n and (s[i] == p[j] or '.' == p[j])
            if j < m - 1 and p[j + 1] == '*':
                cache[(i, j)] = dp(i, j + 2) or (char_match and  dp(i + 1, j))

                return cache[(i, j)]

            if char_match:
                cache[(i, j)] = dp(i + 1, j + 1)
                return cache[(i, j)]

            cache[(i ,j)] = False
            return cache[(i ,j)]
        
        return dp(0, 0)