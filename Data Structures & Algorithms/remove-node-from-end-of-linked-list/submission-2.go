/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func removeNthFromEnd(head *ListNode, n int) *ListNode {
    dummy := &ListNode{Next: head}
    slow, fast := dummy, dummy

    // move fast n steps ahead
    for i := 0; i < n; i++ {
        fast = fast.Next
    }

    // move both until fast is at last node
    for fast.Next != nil {
        fast = fast.Next
        slow = slow.Next
    }

    // slow.Next is the node to remove
    slow.Next = slow.Next.Next

    return dummy.Next
}
