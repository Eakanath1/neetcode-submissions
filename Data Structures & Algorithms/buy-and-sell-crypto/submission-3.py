class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]
        n = len(prices)
        for i in range(1, n):
            if prices[i] - buy > res:
                res = prices[i] - buy
            elif prices[i] < buy:
                buy = prices[i]
        return res