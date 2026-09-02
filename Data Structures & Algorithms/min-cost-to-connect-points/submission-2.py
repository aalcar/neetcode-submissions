class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # pick an arbitrary start
        # choose smallest at any given state that connects a new one?
        n = len(points)
        seen = set()
        res = node = 0
        connection_costs = [float('inf')] * n

        while len(seen) < n - 1:
            # check all of the neighbors 
            seen.add(node)
            next_node = -1 # don't have a neighbor to go to yet
            for neighbor in range(n):
                if neighbor in seen:
                    continue
                x1, y1 = points[node]
                x2, y2 = points[neighbor]

                dist = abs(x2 - x1) + abs(y2 - y1)
                connection_costs[neighbor] = min(connection_costs[neighbor], dist)

                # set next possible neighbor or closest node
                if next_node == -1 or connection_costs[neighbor] < connection_costs[next_node]:
                    next_node = neighbor

            res += connection_costs[next_node]
            node = next_node
    
        return res