# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    @staticmethod
    def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev  


    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        h2 = self.reverseList(slow.next)
        slow.next = None
        h1 = head
        while h1 and h2:
            nxt1, nxt2 = h1.next, h2.next
            h1.next = h2
            h2.next = nxt1
            h1 = nxt1
            h2 = nxt2
