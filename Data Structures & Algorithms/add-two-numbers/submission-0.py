# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # default carry = 0
        # add the two nums
        # dummy = ListNode()
        # prev = dummy
        # while l1 and l2
            # sum = l1 + l2 + carry
            # carry = sum // 10
            # new_val = sum % 10
            # new = ListNode(new_val)
            # prev.next = new
            # prev = prev.next
            # 100 + 1
            # 2 9 9
            # 9
            # 1 0 0 1
        #
        # [8, 4, 9]
        # [7, 7, 5]
        # [5, ]
        carry = 0
        dummy = ListNode()
        prev = dummy
        while l1 and l2:
            summed = l1.val + l2.val + carry
            carry = summed // 10
            new_val = summed % 10
            new = ListNode(new_val)
            prev.next = new
            prev = prev.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            summed = l1.val + carry
            carry = summed // 10
            new_val = summed % 10
            new = ListNode(new_val)
            prev.next = new
            prev = prev.next
            l1 = l1.next

        while l2:
            summed = l2.val + carry
            carry = summed // 10
            new_val = summed % 10
            new = ListNode(new_val)
            prev.next = new
            prev = prev.next
            l2 = l2.next

        prev.next = ListNode(1) if carry else None

        return dummy.next