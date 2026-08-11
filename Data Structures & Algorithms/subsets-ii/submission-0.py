class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(curr, i):
            if i == len(nums):
                res.append(curr[:])
                return

            curr.append(nums[i])
            backtrack(curr, i + 1)
            curr.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            backtrack(curr, i + 1)

        backtrack([], 0)
        return res