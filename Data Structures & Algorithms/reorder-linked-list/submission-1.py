# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        h2 = slow.next
        slow.next = None
        prev = None
        while h2:
            tmp = h2.next
            h2.next = prev
            prev = h2
            h2 = tmp

        h1, h2 = head, prev
        while h1 and h2:
            nxt1, nxt2 = h1.next, h2.next
            h1.next = h2
            h2.next = nxt1
            h1 = nxt1
            h2 = nxt2
