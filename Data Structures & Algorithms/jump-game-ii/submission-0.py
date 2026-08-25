class Solution:
    def jump(self, nums: List[int]) -> int:
        # 1, 3, 2, 2, 0, 3, 0, 2, 0, 1
        # do we want the range of indices potentially hit
        # OR some optimal range?
        # we can dupe if we can include the same ones
        # and jump to O(N^2), so just do new ones possible?
        res = l = r = 0
        farthest_idx = 0

        while r < len(nums) - 1:
            while l < len(nums) and l <= r:
                farthest_idx = max(farthest_idx, nums[l] + l)
                l += 1

            r = farthest_idx
            res += 1

        return res