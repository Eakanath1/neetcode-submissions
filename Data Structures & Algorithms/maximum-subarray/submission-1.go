func maxSubArray(nums []int) int {
    res, curSum := nums[0], nums[0]
    n := len(nums)
    for i := 1; i < n; i++ {
        curSum += nums[i]
        if curSum < nums[i] {
            curSum = nums[i]
        }
        res = max(res, curSum)
    }
    return res
}
