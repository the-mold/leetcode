class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
       # dp[i] will store the number of combinations that sum to i.
        # The size is target + 1 to account for sums from 0 to target.
        dp = [0] * (target + 1)
        
        # Base case: There is one way to make a sum of 0 (by choosing no numbers).
        dp[0] = 1
        
        # Build the DP table from 1 up to the target.
        for i in range(1, target + 1):
            # For each sum `i`, check which numbers from `nums` can be used.
            for num in nums:
                # If `i - num` is a valid sum (>= 0), it means we can form
                # the sum `i` by adding `num` to any combination that sums to `i - num`.
                if i - num >= 0:
                    # Add the number of ways to form `i - num` to our current total for `i`.
                    dp[i] += dp[i - num]
                    
        # The final answer is the number of ways to form the target sum.
        return dp[target]
