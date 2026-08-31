class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # so djkstras starting from k
        # return largest distance?
        # can check 
        adj_list = defaultdict(list)
        for u, v, t in times:
            adj_list[u].append((v, t))

        heap = [(0, k)]
        seen = set()

        while heap:
            t1, u = heapq.heappop(heap)

            if u in seen:
                continue

            seen.add(u)
            farthest = t1

            for v, t2 in adj_list[u]:
                if v not in seen:
                    heapq.heappush(heap, (t1 + t2, v))

        return farthest if len(seen) == n else -1
        