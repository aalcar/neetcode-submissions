# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. set up fast and slow to reach the middle (and prev 1 before middle)
        # 2. reverse that segment using prev and slow
        # 3. merge the two linked lists
        #   1. nextNode = start.next
        #   2. set start.next to prev 
        #   3. start.next.next = nextNode
        #   4. start = start.next.next
        #   repeat?

        # point prev at the list that needs to be axed
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Have: 2, 4, 6, 8, 10, 12
        # Want: 2, 4, 6, 12, 10, 8

        # Step by Step
        # prev = initial = 6
        # slow = 8
        # temp = 10
        # slow.next = None
        # prev = 8
        # slow = 10
        # temp = 12
        # slow.next = 8
        # prev = 10
        # slow = 12
        # temp = None
        # prev = 12
        # slow = None
        # initial.next = 12

        # merge 

        # Have: 2, 4, 6, 12, 10, 8
        # Want: 2, 12, 4, 10, 6, 8

        curr, second = head, prev
        while second:
            temp_c = curr.next
            temp_s = second.next

            curr.next = second
            second.next = temp_c

            curr = temp_c
            second = temp_s

        """
        i=12
        c=2
        ti=10
        inext=4
        cnext=12
        curr=4
        i=10
        ti=8
        inext6
        cnext=10
        curr=6
        i=8
        ti=None
        inext=12
        cnext=8
        curr=None
        """

