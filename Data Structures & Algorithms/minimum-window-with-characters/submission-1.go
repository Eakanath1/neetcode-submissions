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

    distinctRequired := 0
	for i := 0; i < 52; i++ {
		if needCount[i] > 0 {
			distinctRequired++
		}
	}

    var winCount [52]int
    winFormed := 0

    resL, resLen := 0, len(s)+1
    l := 0
    for r := 0; r < len(s); r++ {
        x := idx(s[r])
		winCount[x]++

		// Just reached the needed frequency for this char
		if needCount[x] > 0 && winCount[x] == needCount[x] {
			winFormed++
		}

        // Shrink window till the min size at which it is valid
        for l <= r && winFormed == distinctRequired {
            if curLen := r-l+1; curLen < resLen {
                resL = l
                resLen = curLen
            }
            y := idx(s[l])
			// If this char is currently exactly satisfied, removing it will break validity
			if needCount[y] > 0 && winCount[y] == needCount[y] {
				winFormed--
			}
			winCount[y]--
            l++
        }
    }
    if resLen == len(s)+1 {
        return ""
    }
    return s[resL : (resL+resLen)]
}
