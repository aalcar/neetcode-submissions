class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(1) space so probably 2 pointers
        # wait binary search?
        # nah just use two pointers
        l = 0
        r = len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
            