class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # iterate through intervals
        # our new one could start it
        # or end it
        # those would edge cases
        # check your_start and prev_end
        # -- merge prev and yours if they overlap
        # check your_end and next_start 
        # 
        # we do this at beginning as well
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

        # [[1,2],[3,5],[9,10]]
        # input: [0, 1]