func hasDuplicate(nums []int) bool {
    seen := make(map[int]bool)
    for _, num := range nums {
        if _, exists := seen[num]; exists {
            return true
        }
        seen[num] = true
    }
    return false
}
