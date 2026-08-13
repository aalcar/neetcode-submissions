class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(int)
        for start, end in intervals:
            mp[start] += 1
            mp[end] -= 1

        active = 0
        curr_interval = []
        res = []

        for pos in sorted(mp.keys()):
            # initial starting point
            if not curr_interval:
                curr_interval.append(pos)

            active += mp[pos]

            if active == 0:
                curr_interval.append(pos)
                res.append(curr_interval)
                curr_interval = []

        return res