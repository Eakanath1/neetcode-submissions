func missingNumber(nums []int) int {
	// Math can still cause overflow issues at times, XOR of same number is always zero & XOR of any number with 0 is itself
	n := len(nums)
	res := n
	for i, num := range(nums) {
		res ^= i ^ num
	}
	// All existing numbers cancelled out by their index counterparts, only missing number left
	return res
}
