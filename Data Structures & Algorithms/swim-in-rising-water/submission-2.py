class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # instead of sums its max() of the path
        # you can be greedy
        # trying to take a detour will just put you on a route you were gonna go through anyway
        n = len(grid)
        candidates = []
        seen = set()
        max_elev = grid[0][0]
        x, y = 0, 0

        while (x, y) != (n - 1, n - 1):
            if x > 0 and (x - 1, y) not in seen:
                heapq.heappush(candidates, (grid[x - 1][y], x - 1, y))
            if y > 0 and (x, y - 1) not in seen:
                heapq.heappush(candidates, (grid[x][y - 1], x, y - 1))
            if x < n - 1 and (x + 1, y) not in seen:
                heapq.heappush(candidates, (grid[x + 1][y], x + 1, y))
            if y < n - 1 and (x, y + 1) not in seen:
                heapq.heappush(candidates, (grid[x][y + 1], x, y + 1))

            elev, x, y = heapq.heappop(candidates)
            max_elev = max(max_elev, elev)
            seen.add((x, y))

        return max_elev