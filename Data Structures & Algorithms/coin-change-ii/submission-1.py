class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]
        # base case
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1, n+1):
            coin = coins[i-1]
            for money in range(1, amount+1):
                if coin <= money:
                    # Select the coin ways, and don't select
                    dp[i][money] = dp[i][money-coin] + dp[i-1][money]
                else:
                    dp[i][money] = dp[i-1][money]
        return dp[n][amount]