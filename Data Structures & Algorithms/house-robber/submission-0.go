func rob(nums []int) int {
    n := len(nums)
    maxRob := make([]int, n+1)
    maxRob[1] = nums[0]
    for i := 2; i <= n; i++ {
        maxRob[i] = max(maxRob[i-1], maxRob[i-2]+nums[i-1])
    }
    return maxRob[n]
}
