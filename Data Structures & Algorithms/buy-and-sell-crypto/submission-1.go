func maxProfit(prices []int) int {
    res := 0
    buy := 0
    for i, price := range prices {
        if price < prices[buy] {
            buy = i
        } else {
            profit := price - prices[buy]
            res = max(res, profit)
        }
    }
    return res
}
