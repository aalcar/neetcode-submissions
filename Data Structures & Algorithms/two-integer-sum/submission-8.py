class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # just store numbers we've seen before
        # see if the target - current number is in the seen set
        # if it is -> we good
        # if not, just keep going
        # seen set can just be hash table of num -> index   
        seen = {}
        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in seen:
                return [seen[difference], i]
                
            seen[nums[i]] = i
        
        return [-1, -1]