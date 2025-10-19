class Solution:
    def climbStairs(self, n: int) -> int:
        # Create a cache to store the results for each step.
        memo = {}

        def solve(i: int) -> int:
            # Base cases
            if i == 1:
                return 1
            if i == 2:
                return 2
            
            # If we've already calculated the ways to reach step 'i',
            # return the cached result.
            if i in memo:
                return memo[i]
            
            # Recursive step: The number of ways to reach step 'i' is the sum of
            # the ways to reach step 'i-1' and the ways to reach step 'i-2'.
            
            # Why not add one more step to previous counts?
            # Let's think about the very last move you make to land on step n.
            # There are only two possibilities for your final move:
            # - You were on step n-1 and you took a single step of 1.
            # - You were on step n-2 and you took a single step of 2.
            # Since these two scenarios (ending with a 1-step or ending with a 2-step) are mutually exclusive, the total number of ways to reach step n is the sum of the ways to get to those previous positions.
            # We are not counting the length of the steps; we are counting the number of unique sequences of steps. The solve(i-1) function call already represents the total count of ways to get to that previous step. We just need to sum up the counts from the two possible preceding steps.
            
            result = solve(i - 1) + solve(i - 2)
            
            # Cache the result before returning.
            memo[i] = result
            
            return result

        # Handle the initial cases for n=1 and n=2 directly.
        if n <= 2:
            return n
        
        # Start the top-down process from step 'n'.
        return solve(n)

