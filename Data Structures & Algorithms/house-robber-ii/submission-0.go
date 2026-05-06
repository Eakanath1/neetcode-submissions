func rob(nums []int) int {
    n := len(nums)
    if n < 2 {
        return nums[0]
    }
    robPart := func(numsPart []int) int {
        prev2, prev1 := 0, 0
        for _, num := range numsPart {
            cur := max(prev1, prev2+num)
            prev2 = prev1
            prev1 = cur
        }
        return prev1
    }
    return max(robPart(nums[:n-1]), robPart(nums[1:]))
}
