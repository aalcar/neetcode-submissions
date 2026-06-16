class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # first instinct is to use a set to detect a duplicate
        seen = set()

        for num in nums:
            if num in seen:
                return True
                
            seen.add(num)

        return False
