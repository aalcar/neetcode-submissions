class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # [3,2,7,2,0,4,0, 0, 0, 1]
        #. 0 1 2 3 4 5 6. 7. 8. 9
        # track what index we want to reach
        #   -- start at len(nums) - 1
        # iterate backwards seeing if we can reach that
        # then 
        # is there a situation where the previous value gets us there
        # but the one infront doesn't?
        i = len(nums) - 1
        for j in range(len(nums) - 2, -1, -1):
            if j + nums[j] >= i:
                i = j

        return i == 0