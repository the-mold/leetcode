class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0] * (n + 1) #O(n)
        dp[1] = 1

        for i in range(2, n+1): #O(n-1)
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

#T: O(n)
#S: O(1)
