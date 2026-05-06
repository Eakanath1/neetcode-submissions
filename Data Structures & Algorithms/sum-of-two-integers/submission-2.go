func getSum(a int, b int) int {
	// Cast them to 32 bit numbers explicitly
    a32, b32 := int32(a), int32(b)
    for b32 != 0 {
        carry := (a32 & b32) << 1
        sumWithoutCarry := a32 ^ b32
        a32 = sumWithoutCarry
        b32 = carry
    }
    return int(a32)
}
