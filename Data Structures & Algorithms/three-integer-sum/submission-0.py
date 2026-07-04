class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # gonna be O(n^2) anyway, so might as well sort the list
        # then use two pointers after setting one of the digits as a num usable
        # becomes a two-sum problem after 0 - nums[i]
        # need the two-sum to == -nums[i]

        nums.sort()
        result = set()

        for i in range(len(nums)):
            # solve two-sum
            target = -nums[i]
            # start past i to avoid dupes
            l = i + 1
            r = len(nums) - 1
            
            # skip any dupes
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # -4, -2, -1, 0, 3, 4, 5

            while l < r:          
                curSum = nums[l] + nums[r]

                if curSum > target:
                    r -= 1
                elif curSum < target:
                    l += 1
                else:
                    result.add((nums[i], nums[l], nums[r]))
                    r -= 1
                    l += 1

                    # duplicate protection; doesn't matter which pointer moves
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        
        return list(result)