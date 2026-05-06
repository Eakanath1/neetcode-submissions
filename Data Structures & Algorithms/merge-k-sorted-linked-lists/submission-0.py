# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self._mergeRange(lists, 0, len(lists) - 1)
    
    def _mergeRange(
        self,
        lists: List[Optional[ListNode]],
        left: int,
        right: int
    ) -> Optional[ListNode]:
        if left == right:
            return lists[left]
        if left > right:
            return None
        
        mid = (left + right) // 2
        l1 = self._mergeRange(lists, left, mid)
        l2 = self._mergeRange(lists, mid + 1, right)
        return self._mergeTwoLists(l1, l2)
    
    def _mergeTwoLists(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next
