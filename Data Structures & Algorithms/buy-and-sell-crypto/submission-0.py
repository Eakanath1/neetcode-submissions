class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            # If this price is cheaper, update our best buy opportunity
            if price < min_price:
                min_price = price
            else:
                # Otherwise, see if selling today beats our best profit so far
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
        
        return max_profit