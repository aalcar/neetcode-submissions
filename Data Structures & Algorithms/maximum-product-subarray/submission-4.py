class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # my guess:
        # kadane's algorithm but you have to account for current sign?
        # definitely just keep multiplying because you never know
        # 
        # global_max = 0
        # min =(val, min * val, max * val)
        # max = max(val, min * val, max * val)
        # just reuse that pattern again and again
        # -4, -1, -2, -3
        #      4  -8
        #     -1   2
        #         -2
        global_max = float('-inf')
        local_min = 1
        local_max = 1
        for num in nums:
            prev_local_min = local_min
            local_min = min(num, num * local_min, num * local_max)
            local_max = max(num, num * prev_local_min, num * local_max)
            global_max = max(global_max, local_max)
        
        return global_max
        