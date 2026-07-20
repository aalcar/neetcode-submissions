# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # increment n - 1 times
        # remove it
        # ez
        # edge cases:
        # beginning
        # end? (nope, can still )
        # 

        # count size
        size = 0
        curr = head
        while curr:
            curr = curr.next
            size += 1

        dummy = ListNode(0, head)
        curr = dummy
        for _ in range(size - n):
            curr = curr.next
        
        curr.next = curr.next.next

        return dummy.next

        # examples
        # d -> 1 -> 2 -> 3 -> 4
        # c    c
        # d -> 1 -> 3 -> 4
        # return 1 