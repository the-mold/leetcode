class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # state - cost to reach a given step

        # ds
        dp = [0] * (len(cost))

        # relation
        # dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        # base case
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        
        return min(dp[-1], dp[-2])
