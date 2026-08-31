class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # so djkstras starting from k
        # return largest distance?
        # can check 
        adj_list = defaultdict(list)
        time_to = defaultdict(int)
        for u, v, t in times:
            adj_list[u].append(v)
            time_to[(u, v)] = t


        dist = [float('inf')] * n
        heap = [k] # keep going towards closest total dist away
        dist[k - 1] = 0

        while heap:
            u = heapq.heappop(heap)
            for v in adj_list[u]:
                if dist[v - 1] > dist[u - 1] + time_to[(u, v)]:
                    dist[v - 1] = dist[u - 1] + time_to[(u, v)]
                    heapq.heappush(heap, v)

        longest_dist = 0
        for d in dist:
            if d == float('inf'):
                return -1
            longest_dist = max(longest_dist, d)
        return longest_dist
        