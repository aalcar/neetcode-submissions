from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        fn(i, j) -> bool
        rr: if next is *, ret if (i + 1, j){if length permits} or (i, j+2) is good
        if next is not *, check if match, no match is false, match is (i + 1, j + 1)
        base cases: end of s and p reached -> true, end of p but not s -> false
        """
        @cache
        def dp(i, j):
            if j == len(p):
                return i == len(s)
            
            char_match = i < len(s) and (s[i] == p[j] or '.' == p[j])
            if j < len(p) - 1 and p[j + 1] == '*':
                state_1 = False
                if char_match:
                    state_1 = dp(i + 1, j)
                state_2 = dp(i, j + 2)

                return state_1 or state_2
            else:
                if char_match:
                    return dp(i + 1, j + 1)
                else:
                    return False
        
        return dp(0, 0)