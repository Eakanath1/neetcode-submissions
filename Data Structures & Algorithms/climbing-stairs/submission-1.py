class Solution:
    def climbStairs(self, n: int) -> int:
        # Top Down approach
        memo = {}

        def climb(n):
            if n == 0 or n == 1:
                return 1
            if n not in memo:
                memo[n] = climb(n - 1) + climb(n - 2)
            return memo[n]

        return climb(n)