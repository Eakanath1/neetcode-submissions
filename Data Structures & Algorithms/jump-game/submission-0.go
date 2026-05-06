func canJump(nums []int) bool {
    n := len(nums)
    reachable := make([]bool, n)
    reachable[0] = true
    for i := 0; i < n; i++ {
        num := nums[i]
        if reachable[i] {
            for j := i+1; j <= i+num && j < n; j++{
                reachable[j] = true
            }
        }
    }
    return reachable[n-1]
}
