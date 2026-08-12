class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # what I remember:
        # turn the input into some kind of structure
        # adj list, adj matrix, i forgot what else
        # then, use dfs or bfs (forgot how to do those),
        # on the graph
        # dfs is just recursive calls
        # bfs is adding adjacent elements to a q

        # for this problem
        # number of islands is the number of independent dfs calls?
        # what i mean by independent: not called by another dfs
        # called while we traverse
        # we only traverse if we havent visited and its a 1?
        # mark everything we see visited
        def dfs(r, c):
            if (r == ROWS or 
                r < 0 or c == COLS or
                c < 0 or grid[r][c] == "0"
                or (r, c) in seen):
                return

            seen.add((r, c))

            directions = (
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            )

            for direction in directions:
                x_inc, y_inc = direction[0], direction[1]
                dfs(r + x_inc, c + y_inc)

        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        seen = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in seen:
                    count += 1
                    dfs(r, c)

        return count