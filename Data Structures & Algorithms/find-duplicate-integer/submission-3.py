class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use the indices
        slow = nums[nums[0]]
        fast = nums[nums[nums[0]]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # s3 f2
        # 
        
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow