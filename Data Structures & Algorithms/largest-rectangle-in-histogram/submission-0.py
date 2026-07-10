class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # i'm thinking that we're looking left
        # for the smallest element
        # 7, 1
        #
        # i think we can combine with the min rectangle if that's best
        # bc min is always the height that we use, we're sure that it's
        # the height used by itself when it found it's largest rectangle
        # 
        # ex.
        # 7 -> 7
        # 7, 1 -- find the min rect of these two, then pop 7
        # 1 -> 2
        # 1, 7, 7 
        # we look at the stack to see the nearest strictly shortest wall 
        # in O(1)
        # [4, 2, 1, 2, 5, 3]
        n = len(heights)

        stack = []
        left_wall = [] # -1, -1, -1, 2, 3, 3
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            shortest_index = -1 if not stack else stack[-1]
            
            stack.append(i)
            left_wall.append(shortest_index)

        # 4, 2, 1, 2, 5, 3
        stack.clear()   # 1
        right_wall = [] # 6 5 6 6 2 1
        for i in range(n):
            current_index = n - 1 - i
            while stack and heights[stack[-1]]>= heights[current_index]:
                stack.pop()

            shortest_index = n if not stack else stack[-1]

            stack.append(current_index)
            right_wall.append(shortest_index)

        right_wall.reverse()

        # left_wall = -1, -1, -1, 2, 3, 3
        # right_wall = 1,  2,  6, 6, 5, 6 

        maxArea = 0
        for i in range(n):
            area = heights[i] * (right_wall[i] - left_wall[i] - 1)
            maxArea = max(maxArea, area)

        return maxArea
