class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = float('-inf')
        local_min = local_max = 1

        for num in nums:
            prev_local_min = local_min
            local_min = min(num, num * local_min, num * local_max)
            local_max = max(num, num * prev_local_min, num * local_max)
            global_max = max(global_max, local_max)
        
        return global_max
        