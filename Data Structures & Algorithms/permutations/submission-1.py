class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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