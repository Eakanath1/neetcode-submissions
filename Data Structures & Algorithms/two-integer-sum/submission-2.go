func twoSum(nums []int, target int) []int {
    var compMap = make(map[int]int)
    for i, num := range nums {
        if foundIdx, found := compMap[target - num]; found {
            return []int{foundIdx, i}
        }
        compMap[num] = i
    }
    return []int{}
}
