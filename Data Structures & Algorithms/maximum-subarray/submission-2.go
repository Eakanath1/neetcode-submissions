func maxSubArray(nums []int) int {
    // NOTE: We can't write `dfs := func(...) { dfs(...) }` for recursion in Go.
    // With `:=`, `dfs` isn't in scope inside its own function literal during initialization,
    // so recursive calls see "undefined: dfs". Declare first, then assign.
    var dfs func(l, r int) int

    dfs = func(l, r int) int {
		if l == r {
			return nums[l]
		}
		m := l + (r-l)/2

		// 1) best entirely in left half
		leftBest := dfs(l, m)

		// 2) best entirely in right half
		rightBest := dfs(m+1, r)

		// 3) best crossing mid:
		// best suffix ending at m
		sum := 0
		bestLeftSuffix := nums[m]
		for i := m; i >= l; i-- {
			sum += nums[i]
			if sum > bestLeftSuffix {
				bestLeftSuffix = sum
			}
		}

		// best prefix starting at m+1
		sum = 0
		bestRightPrefix := nums[m+1]
		for i := m + 1; i <= r; i++ {
			sum += nums[i]
			if sum > bestRightPrefix {
				bestRightPrefix = sum
			}
		}

		crossBest := bestLeftSuffix + bestRightPrefix

		return max(max(leftBest, rightBest), crossBest)
	}

	return dfs(0, len(nums)-1)
}
