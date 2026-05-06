func threeSum(nums []int) [][]int {
    sort.Ints(nums)
	n := len(nums)
    var res [][]int
    for i := 0; i < n-2; i++ {
        // skip duplicate i
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
        // optimization (optional, only as target is zero): if smallest is > 0, can't sum to 0
		if nums[i] > 0 {
			break
		}
        l, r := i+1, n-1
        for l < r {
            sum := nums[i] + nums[l] + nums[r]
            if sum == 0 {
				res = append(res, []int{nums[i], nums[l], nums[r]})
                l++
                r--
                // skip duplicate l
				for l < r && nums[l] == nums[l-1] {
					l++
				}
                // skip duplicate r
                for l < r && nums[r] == nums[r+1] {
                    r--
                }
            } else if sum < 0 {
                l++
            } else {
                r--
            }
        }
    }
    return res
}