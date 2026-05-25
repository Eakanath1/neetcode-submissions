class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0]*(amount+1)
        # base case, always one way to make nothing
        dp[0] = 1
        for i in range(1, n+1):
            coin = coins[i-1]
            for money in range(1, amount+1):
                if coin <= money:
                    # Select the coin ways, and previous value (don't select current)
                    dp[money] = dp[money-coin] + dp[money]
                # else case dp value remains unchanged during this iter
        return dp[amount]