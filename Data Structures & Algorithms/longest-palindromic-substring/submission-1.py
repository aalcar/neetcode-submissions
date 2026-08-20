class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_len = res_idx = 0

        for i in range(len(s)):
            # check biggest odd palindrome
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res_len:
                    res_len = r - l + 1
                    res_idx = l
                l -= 1
                r += 1

            # check biggest even palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res_len:
                    res_len = r - l + 1
                    res_idx = l
                l -= 1
                r += 1

        return s[res_idx:res_idx + res_len]