class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 0. state - min cost to reach step i

        # 1. data structure. dp has one extra position to represent the cost of reaching the top floor.
        dp = [0] * (len(cost) + 1)

        # 2. relation
        #dp[i] = cost[i] + min(dp[i-2], dp[i-1])
        
        # 3. since we can choose at which step to start, the cost for them is 0
        dp[0] = 0
        dp[1] = 0

        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1]+ cost[i-1])

        return dp[-1]
