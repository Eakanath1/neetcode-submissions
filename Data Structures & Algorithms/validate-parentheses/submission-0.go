func isValid(s string) bool {
    closeToOpen := map[byte]byte{
		')': '(',
		'}': '{',
		']': '[',
	}

	stack := make([]byte, 0, len(s))

	for i := 0; i < len(s); i++ {
		c := s[i]

		// If it's an opening bracket, push it
		if c == '(' || c == '{' || c == '[' {
			stack = append(stack, c)
			continue
		}

		// If it's a closing bracket, it must match the top
		if expectedOpen, isClose := closeToOpen[c]; isClose {
			if len(stack) == 0 {
				return false
			}
			top := stack[len(stack)-1]
			// Pop the element
			stack = stack[:len(stack)-1]
            if top != expectedOpen {
				return false
			}
			continue
		}

	}

	return len(stack) == 0
}