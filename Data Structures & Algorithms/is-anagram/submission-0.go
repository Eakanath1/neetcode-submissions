func isAnagram(s string, t string) bool {
    if len([]rune(s)) != len([]rune(t)){
        return false
    }
    count := make(map[rune]int)
    for _, char := range s {
        count[char]++
    }
    for _, char := range t {
        count[char]--
        if count[char] < 0 {
            return false
        }
    }
    for _, val := range count {
        if val != 0 {
            return false
        }
    }
    return true
}
