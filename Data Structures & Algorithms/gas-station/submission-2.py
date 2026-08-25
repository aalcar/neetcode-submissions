class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # the only time we cant finish is if not enough gas total
        # in every other case, we can just simulate
        # and see where we run out, then start at next gas station
        # if we CANT NOT finish, there's a start somewhere that works
        if sum(gas) < sum(cost):
            return -1

        start = total = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                start = i + 1
                total = 0

        return start