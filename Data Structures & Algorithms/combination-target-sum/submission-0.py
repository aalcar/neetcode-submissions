class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(path, curr_sum, i):
            if curr_sum == target:
                res.append(path[:])
                return
            
            for j in range(i, len(nums)):
                num = nums[j]
                if curr_sum + num <= target:
                    path.append(num)
                    backtrack(path, curr_sum + num, j)
                    path.pop()

        res = []
        backtrack([], 0, 0)
        return res