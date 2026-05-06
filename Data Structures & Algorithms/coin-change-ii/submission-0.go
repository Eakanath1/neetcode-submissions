func change(amount int, coins []int) int {
	n := len(coins)
    dp := make([][]int, n+1)
	for i := 0; i <=n; i++ {
		dp[i] = make([]int, amount+1)
		// Always one way to make 0
		dp[i][0] = 1
	}
	for i := 1; i <=n; i++ {
		cur := coins[i-1]
		for j := 1; j <= amount; j++ {
			// Don't take current coin
			dp[i][j] = dp[i-1][j]
			if cur <= j {
				// Take the current coin unlimited times (dp/recursion)
				dp[i][j] += dp[i][j-cur]
			}
		}
	}
	return dp[n][amount]
}
