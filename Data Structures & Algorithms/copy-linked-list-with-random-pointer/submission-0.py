"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # iterate through, creating initial list
        # AND
        # marking the og -> new in a map
        old_to_new = {}
        old_curr = head
        new_curr = Node(0)
        dummy = new_curr
        while old_curr:
            new_curr.next = Node(old_curr.val)

            old_to_new[old_curr] = new_curr.next

            old_curr = old_curr.next
            new_curr = new_curr.next

        curr = dummy.next
        old = head
        while curr:
            if old.random:
                curr.random = old_to_new[old.random]
            else:
                curr.random = None
            curr = curr.next
            old = old.next

        return dummy.next

        # 3,7,8
        # curr = 3
        # new = 3
        # while 7:
        # new.next = 7
        # old[3] = 3
        # 
        # curr = 7
        # new = 7
        # while 8:
        # new.next = 7
        # old[3] = 3
        #
        # curr = 3
        # new = 3
        # while 7:
        # new.next = 7
        # old[3] = 3