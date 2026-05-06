# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        if length - n == 0:
            return head.next
        prev, temp = None, head
        count = 0
        while temp and count < (length - n):
            prev = temp
            temp = temp.next
            count += 1
        if prev:
            prev.next = temp.next
            temp.next = None
        return head