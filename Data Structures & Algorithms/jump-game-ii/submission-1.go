func jump(nums []int) int {
    n := len(nums)
	if n <= 1 {
		return 0
	}

	steps := 0
	end := 0       // end of current "level" / range reachable with `steps` jumps
	farthest := 0  // farthest reachable while scanning this range

	for i := 0; i < n-1; i++ {
		if i+nums[i] > farthest {
			farthest = i + nums[i]
		}
		if i == end {      // finished scanning current range -> must take a jump
			steps++
			end = farthest
			if end >= n-1 {
				break
			}
		}
	}
	return steps
}
