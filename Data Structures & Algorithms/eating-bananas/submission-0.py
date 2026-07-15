class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # use binary search on k itself
        # h needs to be atleast len(piles)
        # max you can do actually is max(piles)
        # so, 1 -> max(piles)
        # we do max if h = len(piles)
        # the higher h is, the closer we can go to k=1
        # [1,4,3,2] h=9
        # 1 -> 4
        # how do we know what to use lol
        # do binary search and then search array
        # O(log(max(piles)) * len(piles)) for time complexity
        # determine max(piles)
        r = max(piles)
        l = 1
        while l <= r:
            mid = l + (r - l) // 2
            # O(n) -- search piles and see how it holds
            # if it works -> go lower
            # if it doesn't work -> go higer
            # return l
            timeLeft = h
            for pile in piles:
                timeLeft -= math.ceil(pile / mid)

            if timeLeft >= 0:
                r = mid - 1
            else:
                l = mid + 1

        return l