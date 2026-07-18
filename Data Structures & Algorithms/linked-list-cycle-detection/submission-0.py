# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        with a slow and fast pointer:
        the two WILL meet if there is 
        a cycle. the fast will overtake
        and "chase" the slow pointer 1
        step at a time. i.e. they will 
        approach the slow pointer 1 step
        at a time. the they'll eventually
        meet if there is a cycle
        """
        #[1,2]
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False