func lengthOfLIS(nums []int) int {
	// length 0 => no elements yet
    // capacity n
    // tails[i] = smallest possible tail value of an increasing subsequence of length i+1
    tails := make([]int, 0, len(nums))

	for _, x := range nums {
		// lower_bound on [0, len(tails)): first i with tails[i] >= x
		l, r := 0, len(tails)
		for l < r {
			m := l + (r-l)/2
			if tails[m] >= x {
				r = m
			} else {
				l = m + 1
			}
		}

		if l == len(tails) {
			tails = append(tails, x)
		} else {
			tails[l] = x
		}
	}
	return len(tails)
}
