class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # have a window of k + 1 size
        # if there are dups in window, ret true
        seen = set()

        for i in range(k + 1):
            if i == len(nums):
                break
                
            if nums[i] in seen:
                return True

            seen.add(nums[i])
        
        l = 0
        r = k + 1
        
        while r < len(nums):
            seen.remove(nums[l])

            if nums[r] in seen:
                return True

            seen.add(nums[r])

            r += 1
            l += 1

        return False

