class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0:
            return 0
        
        if n == 1:
            return cost[0]

        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return min(dp[n-1], dp[n-2])
    
#solution
# Initialize DP Array: Create a new array, dp, of the same size as the cost array. dp[i] will store the minimum cost to reach step i.
# Set Base Cases:
# dp[0] = cost[0] (The cost to reach the first step is just its own cost).
# dp[1] = cost[1] (The cost to reach the second step is its own cost, as we can start there).
# Build Up the DP Array: Loop from the third step (i = 2) to the end. For each step, apply the recurrence relation: dp[i] = cost[i] + min(dp[i-1], dp[i-2])
# Return Result: The top of the floor is reached from either step n-1 or n-2. The final answer is the minimum of the total costs stored in dp[n-1] and dp[n-2].
# This approach has a time complexity of O(n) and a space complexity of O(n) due to the extra dp array.