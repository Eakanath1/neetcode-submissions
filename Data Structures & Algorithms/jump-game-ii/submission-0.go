func jump(nums []int) int {
    n := len(nums)
    dp := make([]int, n)
    for i := 1; i < n; i++ {
        dp[i] = -1
    }
    for i := 0; i < n; i++ {
        num := nums[i]
        if dp[i] != -1 {
            for j := i+1; j < n && j <= i+num; j++ {
                if dp[j] == -1 {
                    dp[j] = dp[i] + 1
                } else {
                    dp[j] = min(dp[j], dp[i]+1)
                }
            }
        }
    }
    return dp[n-1]   
}
