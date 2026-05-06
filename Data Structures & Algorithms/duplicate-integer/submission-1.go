func hasDuplicate(nums []int) bool {
    set := make(map[int]struct{})
    for _, num := range nums {
        if _, exists := set[num]; exists {
            return true
        }
        set[num] = struct{}{}
    }
    return false
}
