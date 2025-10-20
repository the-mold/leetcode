class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = {
            # we know that there is no cost to get to the first two stairs
            0: 0,
            1: 0
        }

        def solve(k):
            if k in cache:
                return cache[k]
            
            # find the minimum what it takes to one of the previous steps + its own cost.
            res = min(cost[k-1] + solve(k-1),
                      cost[k-2] + solve(k-2))
            cache[k] = res
            return res

        return solve(n)
