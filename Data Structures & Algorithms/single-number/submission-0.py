class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR
        res = 0
        for num in nums:
            res = num ^ res
        
        return res