class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # length of shortest interval
        # where query[j] overlaps
        # overlapping: counts as inclusive

        res = [-1] * len(queries)
        heap = []

        sorted_query_pairs = [(v, i) for i, v in enumerate(queries)]
        sorted_query_pairs.sort()
        
        intervals.sort()

        interval_idx = 0
        for query, query_idx in sorted_query_pairs:
            while interval_idx < len(intervals) and intervals[interval_idx][0] <= query:
                start, end = intervals[interval_idx]
                heapq.heappush(heap, (end - start + 1, end))
                interval_idx += 1
            # overlaps
            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            
            res[query_idx] = heap[0][0] if heap else -1
            
        return res