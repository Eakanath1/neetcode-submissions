func maxProduct(nums []int) int {
    res := nums[0]
    curMax, curMin := nums[0], nums[0]
    for i := 1; i < len(nums); i++ {
        num := nums[i]
        prevMax, prevMin := curMax, curMin
        curMax = max(num, max(prevMax*num, prevMin*num))
        curMin = min(num, min(prevMax*num, prevMin*num))
        res = max(res, curMax)
    }
    return res
}
