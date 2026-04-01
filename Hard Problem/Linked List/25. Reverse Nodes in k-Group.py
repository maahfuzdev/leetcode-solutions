# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        # Helper function to reverse a part of the list
        def reverse(start, end):
            prev, curr = None, start
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev  # new head of reversed list

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # find the kth node
            kth = group_prev
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # reached end

            group_next = kth.next

            # reverse current k-group
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # connect previous part with reversed group
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp