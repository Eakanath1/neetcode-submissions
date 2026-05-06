# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        # advance first n+1 times
        for _ in range(n+1):
            first = first.next

        # move both until first hits the end
        while first:
            first = first.next
            second = second.next

        # second.next is the node to delete
        second.next = second.next.next
        return dummy.next