class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            dist = x * x + y * y
            heapq.heappush(heap, [-dist, x, y])
            if len(heap) > k:
                heapq.heappop(heap)

        return [[tup[1], tup[2]] for tup in heap]
        