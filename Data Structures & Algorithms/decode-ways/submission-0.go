func numDecodings(s string) int {
    n := len(s)
    prev2 := 1
    prev1 := 0
    if s[0] != '0' {
        prev1 = 1
    } else {
        return 0
    }
    for i := 2; i <= n; i++ {
        cur := 0
        // 1-digit: s[i-1]
        if s[i-1] != '0' {
            cur += prev1
        }
        // 2-digit: s[i-2:i]
        two := (s[i-2]-'0')*10 + (s[i-1]-'0')
        if two >= 10 && two <= 26 {
            cur += prev2
        }
        prev2, prev1 = prev1, cur
    }
    return prev1
}