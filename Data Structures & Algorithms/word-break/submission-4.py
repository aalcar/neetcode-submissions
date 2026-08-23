class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bottom up
        # dp[i] = s[i:] can be broken
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                # if we know the string breaks properly on this end, dont check more
                if dp[i]:
                    break
            
        return dp[0]