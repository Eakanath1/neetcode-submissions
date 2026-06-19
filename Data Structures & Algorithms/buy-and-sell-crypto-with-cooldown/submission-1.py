class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # edge case: need at least 2 days to make a trade
        if n < 2:
            return 0
        # Best profit while holding a stock on day i. Negative because buying costs money.
        hold = [0]*n
        # day 0: only action possible is buying → profit = –price[0]
        hold[0] = -prices[0]
        # Best profit if we sell on day i. Starts cooldown, can't buy tomorrow.
        sold = [0]*n
        # Best profit while resting on day i. Cooldown passed, free to buy.
        free = [0]*n
        for i in range(1, n):
            # keep holding from yesterday OR buy today (only if free yesterday)
            hold[i] = max(hold[i-1], free[i-1]-prices[i])
            # sell today: was holding yesterday + collect today's price
            sold[i] = prices[i] + hold[i-1]
            # stay rested from yesterday OR cooldown just expired (sold yesterday)
            free[i] = max(free[i-1], sold[i-1])
        # answer: best profit when not holding at the end
        return max(sold[n-1], free[n-1])