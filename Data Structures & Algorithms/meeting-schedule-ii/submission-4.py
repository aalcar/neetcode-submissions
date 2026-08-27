"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        heap = [float('inf')]
        res = 0

        for interval in intervals:
            if interval.start < heap[0]:
                res += 1
            else:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)

        return res
