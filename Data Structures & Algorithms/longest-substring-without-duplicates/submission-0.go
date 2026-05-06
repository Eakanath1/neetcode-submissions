func lengthOfLongestSubstring(s string) int {
    posMap := make(map[byte]int)
    res := 0
    windowStart, windowEnd := 0, 0
    for windowEnd < len(s) {
        cur := s[windowEnd]
        // Reset window to the last occurence of this character to avoid repetition
        if prevPos, found := posMap[cur]; found && prevPos >= windowStart {
            windowStart = prevPos + 1
        }
        if res < (windowEnd-windowStart+1) {
            res = windowEnd-windowStart+1
        }
        posMap[cur] = windowEnd
        windowEnd++
    }
    return res
}
