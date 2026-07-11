from heapq import *
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # we can maintain a set of the elements in each window...
        # 1, 2
        # How do we find max in O(1)?
        # brute force ->
        # create a window
        # set of elements in window
        # for each window,
        #   find max elem in set
        # return list of those elements
        # 
        # lets say we have 
        # [1,2,1] -- how do we know when there's a max in a window and when
        # that max changes?
        # [2,1,0] -- we can track the pos of maxes?
        # we only really care about the left and right of the window
        # left is leaving, right is coming in
        # we need to maintain freq?
        # for example, after an element leaves from the left, an element in the middle could
        # become the max
        # so it's not just tracking the left and right positions
        # 
        # we do need to track frequencies
        # 1: 2, 2: 1
        # 1: 1, 2:1, 0:1
        # 
        # we just need to be checking "Does max change from X leaving and Y entering?"
        # That depends on the frequency of X
        # not really though
        # for example, 6, 4, 2 .. 3
        # 4 becomes the max here
        # i'm thinking heap but it's not a heap
        # 
        # monotonic stack?
        # "Does max change from X leaving and Y entering?" is a loaded question
        # because it depends on the elements in between.
        # guess it's a heap lol
        # push negative elems on
        # when taking off, negate them again
        # elem just has to be greater than or equal to left to be valid
        heap = []
        res = []
        l = 0
        # [1,2,1,0,4,2,6]
        # heap = [(-2,1)(-1,0)(-1,2)(0,3)]
        # [2, 2, ]
        for r in range(len(nums)):
            if r < k - 1:
                heappush(heap, (-nums[r], r))
                continue

            heappush(heap, (-nums[r], r))

            while heap[0][1] < l:
                heappop(heap)

            max_element = -heap[0][0]
            res.append(max_element)

            l += 1

        return res


