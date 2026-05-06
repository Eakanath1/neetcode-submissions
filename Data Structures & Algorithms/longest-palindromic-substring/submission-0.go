func longestPalindrome(s string) string {
    if len(s) <= 1 {
		return s
	}
    bestL, bestR := 0, 0
    expand := func(l, r int) {
        // if initial pair invalid, do nothing
        if l < 0 || r >= len(s) || s[l] != s[r] {
            return
        }
        for l > 0 && r+1 < len(s) && s[l-1] == s[r+1] {
            l--
            r++
        }
        if r-l > bestR-bestL {
            bestL, bestR = l, r
        }
    }
    for i := 0; i < len(s); i++ {
		expand(i, i)     // odd length
		expand(i, i+1)   // even length
	}
    return s[bestL : bestR+1]
}
