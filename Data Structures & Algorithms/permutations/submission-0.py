class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # pick a number
        # pick another number
        # pick another number
        # keep doing that until you run out of unique numbers
        #
        # we should build these permutations one piece at a time
        # in "parallel"
        #
        res = []
        def backtrack(permutation):
            if len(permutation) == len(nums):
                res.append(permutation[:])
                return

            for num in nums:
                if num not in permutation:
                    permutation.append(num)
                    backtrack(permutation)
                    permutation.pop()
                    
        backtrack([])
        return res