func minWindow(s string, t string) string {
    if len(t) == 0 || len(s) < len(t) {
		return ""
	}

    // Map letters to 0..51
	idx := func(char byte) int {
		if char >= 'A' && char <= 'Z' {
			return int(char - 'A')
		}
		return int(char-'a') + 26
	}

    // Maintain min count required per char in the substring
    var needCount [52]int
    for i := range(t) {
        needCount[idx(t[i])]++
    }

    var winCount [52]int
    // Validity check if the window has all chars at min. req. freq
    minCountValid := func() bool {
        for i := 0; i < 52; i++ {
            if winCount[i] < needCount[i] {
                return false
            }
        }
        return true
    }

    resL, resLen := 0, len(s)+1
    l := 0
    for r := 0; r < len(s); r++ {
        winCount[idx(s[r])]++

        // Shrink window till the min size at which it is valid
        for l <= r && minCountValid() {
            if curLen := r-l+1; curLen < resLen {
                resL = l
                resLen = curLen
            }
            winCount[idx(s[l])]--
            l++
        }
    }
    if resLen == len(s)+1 {
        return ""
    }
    return s[resL : (resL+resLen)]
}
