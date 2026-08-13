class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi source bfs
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        time = fresh = 0

        def addCell(r, c):
            if (r == ROWS or 
                    c == COLS or 
                    min(r, c) < 0 or
                    grid[r][c] != 1):
                return

            nonlocal fresh

            q.append((r, c))
            grid[r][c] = 2
            fresh -= 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        # multi source bfs on all the rotten oranges
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)

            time += 1
        
        return time if fresh == 0 else -1


# class Solution:
    # def orangesRotting(self, grid: List[List[int]]) -> int:
    #     # multi source bfs
    #     ROWS, COLS = len(grid), len(grid[0])
    #     q = deque()
    #     time = fresh = 0

    #     def addCell(r, c):
    #         if (r == ROWS or 
    #                 c == COLS or 
    #                 min(r, c) < 0 or
    #                 grid[r][c] != 1):
    #             return

    #         q.append((r, c))
    #         grid[r][c] = 2
    #         fresh -= 1

    #     for r in range(ROWS):
    #         for c in range(COLS):
    #             if grid[r][c] == 2:
    #                 q.append((r, c))
    #             if grid[r][c] == 1:
    #                 fresh += 1

    #     # multi source bfs on all the rotten oranges
    #     time = 0
    #     while q:
    #         for _ in range(len(q)):
    #             r, c = q.popleft()
    #             addCell(r + 1, c)
    #             addCell(r - 1, c)
    #             addCell(r, c + 1)
    #             addCell(r, c - 1)

    #         time += 1
        
    #     for r in range(ROWS):
    #         for c in range(COLS):
    #             if grid[r][c] == 1:
    #                 return -1

    #     return time