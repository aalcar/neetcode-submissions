class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Obvious way is just multiply everything together as a single product
        # then append that divided by the current num to the array
        # product = math.prod(nums)
        # for num in nums:
        #   result.append(product / num)
        # return result

        # How do I do it in O(n) time without division?
        # bit operation?

        n = len(nums)

        if n == 0:
            return []

        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        suffix = [1] * n
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        # [3, 2, 1]

        result = [1] * n
        for i in range(n):
            result[i] = prefix[i] * suffix[i]

        # [1, 1, 2, 8]
        # [1, 2, 4, 6]
        # [48, 24, 6, 1]

        # [a, ab, abc, abcd]
        # [abcd, bcd, cd, d]

        # bcd, acd, abd, abc
        return result

