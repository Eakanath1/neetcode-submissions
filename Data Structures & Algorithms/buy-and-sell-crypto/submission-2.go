func maxProfit(prices []int) int {
    if len(prices) == 0 {
        return 0
    }

    res := 0
    minPrice := prices[0]
    for _, price := range prices {
        if price < minPrice {
            minPrice = price
        } else {
            res = max(res, price - minPrice)
        }
    }
    return res
}
