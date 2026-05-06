func characterReplacement(s string, k int) int {
    var cnt [26]int
    windowStart, maxFreq, res := 0, 0, 0
    for windowEnd := 0; windowEnd < len(s); windowEnd++ {
		idx := s[windowEnd] - 'A'
		cnt[idx]++
		if cnt[idx] > maxFreq {
			maxFreq = cnt[idx]
		}

		// if replacements needed > k, shrink
		for (windowEnd-windowStart+1)-maxFreq > k {
			cnt[s[windowStart]-'A']--
			windowStart++
		}

		if windowEnd-windowStart+1 > res {
			res = windowEnd - windowStart + 1
		}
	}
	return res
}
