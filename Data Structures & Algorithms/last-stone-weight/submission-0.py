class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-w for w in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            # x is always bigger or equal
            res_w = x - y
            heapq.heappush(heap, res_w)

        return -heap[0]