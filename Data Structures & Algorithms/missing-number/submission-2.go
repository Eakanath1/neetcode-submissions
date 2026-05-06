func missingNumber(nums []int) int {
	n := len(nums)
	expectedSum := (n*(n+1))/2
	curSum := 0
	for _, num := range(nums) {
		curSum += num
	}
	return (expectedSum - curSum)
}
