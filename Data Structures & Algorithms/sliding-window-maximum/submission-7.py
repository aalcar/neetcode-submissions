from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        l = r = 0
        while r < len(nums):
            # q is no longer in window..
            # what do we do for:
            # 1. no longer in window -- popleft
            # 2. next elem greater -- pop everything
            # 3. next elem -- append
            # [7,2,4], k=2
            # q_of_indices = [0] -- nonincreasing 
            # res = [7,]
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            
            q.append(r)

            if q and q[0] < l: 
                q.popleft()

            if r - l + 1 == k:
                res.append(nums[q[0]])
                l += 1

            r += 1

        return res
            


