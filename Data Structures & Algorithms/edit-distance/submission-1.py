from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        my logic:
        go path of least resistance to minimize
        if equal: move i and j
        -- keys, ley
        good case: dp(i + 1, j + 1)
        insert: dp(i, j + 1) + 1
        delete: dp(i + 1, j) + 1
        replace: dp(i + 1, j + 1) + 1
        """
        @cache
        def dfs(i, j):
            if i == len(word1):
                return len(word2[j:])

            if j == len(word2):
                return len(word1[i:])

            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)

            return 1 + min(dfs(i + 1, j + 1), dfs(i, j + 1), dfs(i + 1, j))

        return dfs(0, 0)
