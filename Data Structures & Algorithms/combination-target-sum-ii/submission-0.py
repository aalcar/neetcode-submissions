class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort and skip adjacent vals if we didnt add
        # val to curr_nums
        def backtrack(curr_nums, curr_sum, i):
            if curr_sum == target:
                res.append(curr_nums[:])
                return
            
            if curr_sum > target or i == len(candidates):
                return

            # add
            curr_nums.append(candidates[i])
            backtrack(curr_nums, curr_sum + candidates[i], i + 1)
            curr_nums.pop()
            # skip
            # -- cases of 1 or more val are already
            # -- handled by add case
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(curr_nums, curr_sum, i + 1)

        res = []
        candidates.sort()
        backtrack([], 0, 0)
        return res