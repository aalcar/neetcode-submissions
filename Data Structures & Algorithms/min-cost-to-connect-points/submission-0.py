class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # pick an arbitrary start
        # choose smallest at any given state that connects a new one?
        seen = set()
        res = 0
        candidates = [(0, 0)] # dist, node
        adj = defaultdict(list)
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                d = abs(x2 - x1) + abs(y2 - y1)
                adj[i].append((d, j))
                adj[j].append((d, i))

        while len(seen) < n:
            dist, node = heapq.heappop(candidates)
            if node in seen:
                continue
            
            res += dist
            seen.add(node)

            for neighbor_cost, neighbor in adj[node]:
                heapq.heappush(candidates, (neighbor_cost, neighbor))
    
        return res