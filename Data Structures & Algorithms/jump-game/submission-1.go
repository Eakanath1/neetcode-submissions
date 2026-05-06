func canJump(nums []int) bool {
    n := len(nums)
    maxReachableIdx := 0
    for i := 0; i < n; i++ {
        if i <= maxReachableIdx && i+nums[i] > maxReachableIdx {
            maxReachableIdx = i+nums[i]
        }
    }
    return (maxReachableIdx >= n-1)
}
