class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we want widest and tallest
        # just start two pointers
        # we'll move pointer that points at smaller bar
        maxArea = 0

        l, r = 0, len(heights) - 1
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maxArea = max(maxArea, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxArea
