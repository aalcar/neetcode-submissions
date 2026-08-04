class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 4th largest = 2
        # k - 1 elements below it
        # all larger
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, num)

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return max_heap[0]