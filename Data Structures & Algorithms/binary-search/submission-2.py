class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # sorted, need to search in O(lgn)
        # that's binary search
        # main thing to consider is probably:
        # when n is even, do we check the left_mid or right_mid?
        # 4 / 2 == 2 [1,2,3,4] (r + l) / 2 tells us right_mid
        # 5 // 2 == 2 
        # looks like (r + l) // 2
        # what about for integer overflow
        # 
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2 

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        # -1,0,2,4,6,8
        # target=3
        # l=0,r=5
        # mid=2
        # nums[mid]=2 < 3
        # l=2,r=5
        # mid=3
        # nums[mid] = 4
        # l=2,r=3
        # mid=2
        # 

        return -1