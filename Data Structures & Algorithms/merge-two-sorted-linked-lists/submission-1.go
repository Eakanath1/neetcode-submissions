/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    res := &ListNode{}
	tail := res

	cur1, cur2 := list1, list2
	for cur1 != nil && cur2 != nil {
		if cur1.Val <= cur2.Val {
			tail.Next = cur1
			cur1 = cur1.Next
		} else {
			tail.Next = cur2
			cur2 = cur2.Next
		}
		tail = tail.Next
	}

	if cur1 != nil {
		tail.Next = cur1
	} else {
		tail.Next = cur2
	}

	return res.Next
}
