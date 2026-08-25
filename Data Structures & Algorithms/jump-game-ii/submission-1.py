class Solution:
    def jump(self, nums: List[int]) -> int:
        res = l = r = 0
        farthest_idx = 0

        while r < len(nums) - 1:
            while l < len(nums) and l <= r:
                farthest_idx = max(farthest_idx, nums[l] + l)
                l += 1

            r = farthest_idx
            res += 1

        return res