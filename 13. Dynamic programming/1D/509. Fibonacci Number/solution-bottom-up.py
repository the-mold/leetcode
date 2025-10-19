class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return n
        if n == 1:
            return n

        # state - sum of previous two numbers at index i

        # 1. data structure.
        # dp has length n + 1 because we need to store the Fibonacci value for every number from 0 to n (inclusive).
        dp = [0] * (n+1)

        # 2. relation
        #dp[i] = dp[i-1]+dp[i-2]

        # base case
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]

        return dp[n]

#T: O(n)
#S: O(1)
