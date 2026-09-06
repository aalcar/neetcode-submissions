class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        dfs(curr, i) -> ways to get sum
        res = dfs(curr - nums[i], i + 1) + dfs(curr + nums[i], i + 1)
        base case: i > len, +0, curr == target and i == len
        """
        dp = defaultdict(int)
        def dfs(curr, i):
            if (curr, i) in dp:
                return dp[(curr, i)]

            if i == len(nums):
                return curr == target

            dp[(curr - nums[i], i + 1)] = dfs(curr - nums[i], i + 1)
            dp[(curr + nums[i], i + 1)] = dfs(curr + nums[i], i + 1)

            return dp[(curr - nums[i], i + 1)] + dp[(curr + nums[i], i + 1)]

        return dfs(0, 0)