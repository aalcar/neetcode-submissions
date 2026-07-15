class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # in a rotated sorted array
        # 1. left portion is always bigger than right portion
        # 2. in right portion, nums to the right are bigger
        # in a sorted subarray, nums[l] is <= num[r]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            # essentially we'd like to know if we're in the right
            # or left portion to know how to proceed right?
            # if we're in the left portion,

            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[l]:
                if nums[mid] < target or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] > target or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

        # [1, 4, 5, 7, 10, -10, -3], target = 10
        # []