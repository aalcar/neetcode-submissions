class Solution:
    def rob(self, nums: List[int]) -> int:
        # when rob(i), you have 2 choices:
        # get i and rob(i + 2)
        # rob(i + 1)
        # rob(i) = max(num[i] + rob(i + 2), rob(i + 1))
        # if we robbed 0 and n-1, choose max to add to our total
        # subtract smallest
        def helper(nums):
            rob1 = rob2 = 0

            for n in nums:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp

            return rob2

        res = max(helper(nums[:len(nums) - 1]), helper(nums[1:]))

        return res if len(nums) > 1 else nums[0]