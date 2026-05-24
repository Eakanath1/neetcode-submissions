class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [None] * (amount + 1)

        # Base case: 0 coins are needed to make amount 0
        dp[0] = 0

        for coin in coins:
            for money in range(1, amount + 1):
                prev = dp[money]
                if coin <= money and dp[money - coin] is not None:
                    cur = dp[money - coin] + 1
                    dp[money] = min(prev, cur) if prev is not None else cur

        return dp[amount] if dp[amount] is not None else -1