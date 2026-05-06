func maxArea(heights []int) int {
    l, r := 0, len(heights)-1
    res := 0
    for l < r {
        hL, hR := heights[l], heights[r]
        width := r-l
        if hL < hR {
            res = max(res, hL*width)
            l++
        } else {
            res = max(res, hR*width)
            r--
        }
    }
    return res
}
