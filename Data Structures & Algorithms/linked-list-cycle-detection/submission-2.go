/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func hasCycle(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return false
	}
    cur := head
    occur := make(map[*ListNode]int)
    for cur != nil {
        if _, ok := occur[cur]; ok {
            return true
        }
        occur[cur]++
        cur = cur.Next
    }
    return false
}
