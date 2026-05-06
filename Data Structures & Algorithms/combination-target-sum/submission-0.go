func combinationSum(nums []int, target int) [][]int {
    n := len(nums)

	// dp[i][t] = list of combinations that sum to t using nums[0..i-1]
	dp := make([][][][]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = make([][][]int, target+1)
        // Base case: sum 0 can always be made with empty combination
        dp[i][0] = [][]int{[]int{}}
    }

    for i := 1; i <= n; i++ {
		x := nums[i-1]
		for t := 1; t <= target; t++ {
			// 1) Exclude x: carry over all combos from previous row
			if len(dp[i-1][t]) > 0 {
				// Deep-copy combos so later appends don't mutate shared slices
				for _, comb := range dp[i-1][t] {
					dp[i][t] = append(dp[i][t], cloneSlice(comb))
				}
			}

			// 2) Include x (unbounded): extend combos from same row at (t - x)
			if t >= x && len(dp[i][t-x]) > 0 {
				for _, comb := range dp[i][t-x] {
					newComb := append(cloneSlice(comb), x)
					dp[i][t] = append(dp[i][t], newComb)
				}
			}
		}
	}

	return dp[n][target]
}

func cloneSlice(a []int) []int {
	if a == nil {
		return nil
	}
	b := make([]int, len(a))
	copy(b, a)
	return b
}