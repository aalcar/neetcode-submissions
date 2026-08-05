"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda interval: interval.start)
        # 0,4 5,10 9,20
        # 4 < 5?
        for i in range(len(sorted_intervals) - 1):
            if sorted_intervals[i].end > sorted_intervals[i + 1].start:
                return False
        
        return True