class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # length of longest increasing subsequence 
        # up to i
        # j is index of last inserted element
        dp = [[-1] * len(nums) for _ in range(len(nums))]

        def dfs(i, j):
            if i == len(nums):
                return 0

            if dp[i][j] != -1:
                return dp[i][j]
            
            left = 0
            if j == -1 or nums[i] > nums[j]:
                left = 1 + dfs(i + 1, i)
            right = dfs(i + 1, j)

            dp[i][j] = max(left, right)
            return dp[i][j]

        return dfs(0, -1)
            
