# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Collect values into an array — one pass, then O(1) indexed access
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        
        n = len(vals)
        res = 0
        for i in range(n // 2):
            res = max(res, vals[i] + vals[n - 1 - i])
        return res