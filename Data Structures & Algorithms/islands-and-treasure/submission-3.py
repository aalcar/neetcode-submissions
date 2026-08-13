class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2 ** 31 - 1
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()

        def validate_add(r, c):
            if (r == ROWS or c == COLS or min(r, c) < 0 or 
                    (r, c) in visited or grid[r][c] != INF):
                return

            visited.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                   q.append([r, c])
                   visited.add((r, c))

        dist = 0
        while q:
            for _ in range(len(q)):
                # only add valid land
                r, c = q.popleft()
                grid[r][c] = dist

                validate_add(r + 1, c)
                validate_add(r - 1, c)
                validate_add(r, c + 1)
                validate_add(r, c - 1)

            dist += 1