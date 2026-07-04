class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLength = 0
        # consider each element from the array as the start of the sequence
        for num in nums:
            # sequence starter.. so just look for elems to add?
            if num - 1 not in numSet:
                curr = num
                length = 1
                while curr + 1 in numSet:
                    length += 1
                    curr += 1

                maxLength = max(maxLength, length)
        return maxLength


        # Input: nums = [0,3,2,5,4,6,1,1]
        # set = (0, 3, 2, 5, 4, 6, 1)
        #