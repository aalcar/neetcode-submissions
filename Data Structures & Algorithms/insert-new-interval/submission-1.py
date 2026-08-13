class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)
        i = 0

        # add any non-overlapping
        while i < n and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1

        # merge all of the intervals that overlap, add once
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # add the rest of the intervals
        while i < n:
            res.append(intervals[i])
            i += 1

        return res