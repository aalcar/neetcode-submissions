# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # see if we can increment k
        # if we can, reverse up to it
        # then go k more
        # reverse those
        # 
        # iterate through list
        # while curr:
        #   ahead = curr
        #   for k - 1
        #       if not ahead
        #           # reached place where no more reversals are needed
        #           return dummy.next
        #       increment
        #   # need a prev node
        #   

        # 1,2,3,4,5,6
        # 1,5,4,3,2,6
        # initial_prev = prev
        # initial_curr = curr
        # while curr != the thing ahead.next
        #   temp = curr.next
        #   curr.next = prev
        #   curr = temp
        # 
        # initial_curr.next = curr
        # initial_prev.next = prev
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:
            # ahead = self.get_kth_node(group_prev, k)
            ahead = group_prev
            i = k
            while ahead and i > 0:
                ahead = ahead.next
                i -= 1

            if not ahead:
                break

            group_next = ahead.next

            prev, curr = ahead.next, group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = group_prev.next
            group_prev.next = ahead
            group_prev = temp

        return dummy.next

    def get_kth_node(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
        