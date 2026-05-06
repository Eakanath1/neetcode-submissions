func wordBreak(s string, wordDict []string) bool {
	dict := make(map[string]bool, len(wordDict))
    for _, word := range wordDict {
        dict[word] = true
    }
    n := len(s)
    // dp[i] means: s[:i] can be segmented into words from dict.
    dp := make([]bool, n+1)
    // base case: empty prefix is segmentable
    dp[0] = true

    for i := 1; i <= n; i++ {
        // Try to end a word at position i; j is the previous cut position.
        for j := 0; j < i; j++ {
            if dp[j] {
                // valid breakpoint found, both parts in dict
                if _, ok := dict[s[j:i]]; ok {
                    dp[i] = true
                    break
                }
            }
        }
    }

    return dp[n]
}
