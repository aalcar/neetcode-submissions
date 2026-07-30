# we initialize with k? hmm
import heapq
class KthLargest:
    # a min heap with k elems, topmost is kth largest
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums.copy()
        self.k = k
        heapq.heapify(self.heap)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]
        

# k = 3, so we're looking at 3rd largest
# if less than k elements....idk
# ohhh we initialize with atleast k always
# so like 4,4,4
# when we add, we return
# we cant just pop a bunch of times
# we could do a min heap with k - 1 elements below ours
# 1 2 3 4 k = 3
# kth largest = 2
# add 1
# 1 1 2 3 4 kth largest = 2
# 1111111111111111111111234 kth largest = 2
# kth largest only changes when we add something bigger...
# less than or equal doesnt change it
# when we add something bigger, pop min and add our guy.
# uhhh but our dude is there?
# ohhh
# 1 2 3 4 5 k = 3
# kth_largest = 3
# if anything bigger, it's not three anymore
# ok yeah its that