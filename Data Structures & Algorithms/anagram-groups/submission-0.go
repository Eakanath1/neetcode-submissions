func groupAnagrams(strs []string) [][]string {
    buckets := make(map[[26]int][]string)
    idx := func (char byte) int {
        return int(char - 'a')
    }
    for _, str := range strs {
        var bucket [26]int
        for i := range str {
            bucket[idx(str[i])]++
        }
        buckets[bucket] = append(buckets[bucket], str)
    }
    res := make([][]string, 0, len(buckets))
    for _, group := range buckets {
        res = append(res, group)
    }
    return res
}
