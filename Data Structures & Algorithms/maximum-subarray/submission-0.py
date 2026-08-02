class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        count = 0
        for num in nums:
            count += num;
            
            max_sum = max(count,max_sum)

            if count < 0:
                count = 0

        return max_sum