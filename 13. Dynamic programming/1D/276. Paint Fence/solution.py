class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k

        # state - number of ways to paint a certain post

        # ds
        dp = [0] * (n + 1)

        # relation
        #dp[i] = (k - 1) * (dp[i-1] + dp[i-2])

        # base case
        dp[1] = k
        dp[2] = k * k # since we are allowed to paint have two posts in a row be the same color

        for i in range(3, n + 1):
            # here (k-1) to use a different color starting from the third pole
            dp[i] = (k - 1) * (dp[i-1] + dp[i-2])

        return dp[n]

# T:O(n)
# S:O(n)
