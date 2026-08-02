class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = [(-math.sqrt(points[i][0] * points[i][0] + points[i][1] * points[i][1]), points[i]) for i in range(len(points))]

        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)

        return [tup[1] for tup in heap]
        