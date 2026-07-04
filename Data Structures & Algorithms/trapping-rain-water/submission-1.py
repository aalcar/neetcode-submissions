class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointers somehow?
        # lets think
        # min of 2 and 3 is 2. gap is 1, so 2 * 1.
        # but we need to account for the height of each block
        # its 
        # for block inbetween 2 and 3:
        #   result += min(2, 3) - heights[blockIndex]
        #
        # once right is bigger than left, calculate
        # then move left to right
        # and move right until....? just account for the max num seen?  nah
        # -- see if you see a num >=.
        #
        # actually instead of moving left to right, i can use that
        # step as my summation 
        # move left until the next value is less?

        # while left ptr <= left + 1 ptr:
        #   left += 1
        # 
        # move right until...
        # -- a value >= valAt[left] appears?
        # then move left to right and do the summation
        # -- yeah i think that works..
        #   is it O(n^2)
        #       pretty sure it's just ~2n

        # this solution is mad smart
        # implicitly accounts for waterValue < 0 by taking max at each index
        # implicitly accounts for finding min(L, R) by moving the smaller and then operating on it
        l = result = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                result += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                result += rightMax - height[r]
        
        return result
        # result += max(min(leftHeight, maxOnRight) - height[l], 0)
            
