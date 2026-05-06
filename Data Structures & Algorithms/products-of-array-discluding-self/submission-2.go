func productExceptSelf(nums []int) []int {
    n := len(nums)
    prefixProduct, postfixProduct := make([]int, n), make([]int, n)
    prefixProduct[0], postfixProduct[n-1] = 1, 1
    for i := n-2; i >= 0; i-- {
        postfixProduct[i] = postfixProduct[i+1] * nums[i+1]
    }
    for i := 1; i < n; i++ {
        prefixProduct[i] = prefixProduct[i-1] * nums[i-1]
    }
    res := make([]int, n)
    for i := range nums {
       res[i] =  prefixProduct[i] * postfixProduct[i]
    }
    return res
}
