func longestCommonSubsequence(text1 string, text2 string) int {
    n, m := len(text1), len(text2)

	// dp[i][j] = LCS length of prefixes text1[:i] and text2[:j]
	dp := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		// dp[0][*] and dp[*][0] stay 0 (empty prefix)
		dp[i] = make([]int, m+1)
	}

	for i := 1; i <= n; i++ {
		for j := 1; j <= m; j++ {
			if text1[i-1] == text2[j-1] {
				// If the last characters match, we can extend the LCS of the previous prefixes.
				dp[i][j] = dp[i-1][j-1] + 1
			} else {
				// If they don't match, the best LCS must skip one of these last characters:
				// either skip text1[i-1] (look up) or skip text2[j-1] (look left).
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
			}
		}
	}
	return dp[n][m]
}
