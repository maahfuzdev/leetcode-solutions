# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):

        if not head or not head.next or k == 0:
            return head

        # Step 1: find length
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: reduce k
        k = k % length
        if k == 0:
            return head

        # Step 3: make circular
        tail.next = head

        # Step 4: find new tail
        steps = length - k - 1
        new_tail = head

        for _ in range(steps):
            new_tail = new_tail.next

        # Step 5: break circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head