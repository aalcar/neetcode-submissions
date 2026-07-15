class Solution:
    def findMin(self, nums: List[int]) -> int:
        # brute force: linear scan to find min
        # -- not helpful
        # 
        # lets say i knew it was rotated 4 times
        # [3,4,5,6,1,2]
        # that means nums[3] > nums[4]
        # 
        # actually the min is at nums[4] lol
        # so however many times it gets rotated == index to find min
        #
        # how to find how many times rotated or index?
        #
        # in a sorted array, the leftmost element is the minimum
        # ....so for every sorted section we find, see if that local min
        # can be global min?
        # [-11,-3,1,3,4,7,10,21]
        # [1,3,4,7,10,21,-11,-3]
        # so three observations are needed:
        # 1. in a local sorted array, leftmost elem is min.
        # 2. in this problem, there is two sorted portions
        # -- in the left & right portions
        # 3. the left portion is always going to have bigger values
        # 
        # [1,3,4,7,10,21,-11,-3,-1,0]
        # check if we're in the left sorted portion
        # if we are move to the right
        # we can't just "return leftmost of the right portion"
        # we kinda can by just searching left portions of the right lol
        # [1,3,4,7,10,21,-11,-3,-1,0] mins=10
        # [21,-11,-3,-1,0] mins=10, -3 # all values to the right in the right sorted portion are bigger
        # [21, -11] mins=10,-3,21 # 
        # [-11] mins =10,-3,21,-11

        # left portion is bigger than right
        # inside of right, any values to the right of a given val are bigger
        l, r = 0, len(nums) - 1
        res = float('inf')
        while l <= r:
            # if we ever land on a sorted portion
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
        
            # binary search between both portions
            mid = l + (r - l) // 2

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

            res = min(res, nums[mid])
            
        return res

        # [4,5,6,7]
        # []