class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # length of longest increasing subsequence 
        # up to i
        # j is index of last inserted element
        dp = [-1] * len(nums)

        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            
            LIS = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]: 
                    LIS = max(LIS, 1 + dfs(j))

            dp[i] = LIS
            return dp[i] 

        return max(dfs(i) for i in range(len(nums)))
            
