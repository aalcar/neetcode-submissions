class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # start dfs on pacific cells and mark what gets reached
        # start dfs on atlantic cells and mark what gets reached
        # any overlap is a cell that can go to both
        # just reverse the condition to move to heights equal or GREATER
        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, ocean, prev_height):
            if (min(r, c) < 0 or 
                    r == ROWS or 
                    c == COLS or 
                    (r, c) in ocean or
                    prev_height > heights[r][c]):
                return
            
            ocean.add((r, c))
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r + 1, c, ocean, heights[r][c]) 
            dfs(r, c - 1, ocean, heights[r][c]) 
            dfs(r, c + 1, ocean, heights[r][c]) 
        
        # top and bottom wall starts
        for c in range(COLS):
            # prev_height = curr_height at first to add
            dfs(0, c, pac, heights[0][c]) 
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        # left and right wall starts
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0]) 
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        return list(pac & atl)