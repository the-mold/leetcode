class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        memo = {}

        def solve(attempt, curr_sum):
            if attempt >= n:
                return 1 if curr_sum == target else 0

            if (attempt, curr_sum) in memo:
                return memo[(attempt, curr_sum)]

            count = 0
            for points in range(1, k+1):
                count += solve(attempt + 1, curr_sum + points)

            count = count % MOD

            memo[(attempt, curr_sum)] = count
            return count
        
        return solve(0, 0)
      
# Complexity
# Time: O(n · target · k)
# Space: O(n · target) for memo, recursion depth O(n)
