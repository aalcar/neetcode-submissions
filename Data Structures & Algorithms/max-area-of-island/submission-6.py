class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(r, c):
            q = deque([(r, c)])
            visited.add((r, c))
            area = 1
            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r >= 0 and 
                        c >= 0 and 
                        r < ROWS and 
                        c < COLS and 
                        grid[r][c] == 1 and 
                        (r, c) not in visited):
                        q.append((r,c))
                        visited.add((r, c))
                        area += 1

            return area

        maxArea = 0
        visited = set()
        directions = ((0,1), (1,0), (0,-1), (-1,0))
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxArea = max(bfs(r, c), maxArea)

        return maxArea