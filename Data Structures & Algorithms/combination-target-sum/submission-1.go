// DP ends up generating and storing a bunch of intermediate combinations
// and keeps deep-copying them repeatedly, taking significant compute & space

func combinationSum(nums []int, target int) [][]int {
    // Sort now, so we may skip any values which are greater than target early on
    sort.Ints(nums)

    res := [][]int{}
    path := []int{}
    var dfs func(start, remainder int)
    dfs = func(start, remainder int) {
        if remainder == 0 {
            // mk a copy of path
            comb := make([]int, len(path))
            copy(comb, path)
            res = append(res, comb)
            return
        }
        for i := start; i < len(nums); i++ {
            x := nums[i]
            if x > remainder {
                // pruning early due to sorting, if not continue
                break
            }
            // choose
            path = append(path, x)
            // i, not i+1 : reuse allowed
            dfs(i, remainder-x)
            // un-choose (backtrack)
            path = path[:len(path)-1]
        }
    }
    dfs(0, target)
    return res
}