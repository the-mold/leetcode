from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def solve(index: int) -> int:
            """
            Recursively calculates the maximum money that can be robbed
            from the current house (at 'index') to the end of the street.
            """
            # Base Case: If the index is out of bounds, it means there are
            # no more houses to rob, so we gain 0 money.
            if index >= len(nums):
                return 0
            
            # --- Two Choices for the current house ---
            
            # Choice 1: Rob the current house.
            # The total money will be the current house's money plus the maximum
            # we can get by robbing from the house at `index + 2` onwards.
            rob_this_house = nums[index] + solve(index + 2)
            
            # Choice 2: Skip the current house.
            # The total money will be the maximum we can get by robbing
            # from the very next house at `index + 1` onwards.
            skip_this_house = solve(index + 1)
            
            # Return the better of the two choices.
            return max(rob_this_house, skip_this_house)

        # Start the process from the first house (index 0).
        return solve(0)
  
# Time Complexity: O(2^n)
# This solution has exponential time complexity. For each house, the function branches into two recursive calls, leading to a tree of possibilities that grows exponentially with the number of houses n.
# It's very inefficient because it re-computes the same subproblems over and over again (e.g., solve(3) will be calculated multiple times through different paths). This is exactly the problem that dynamic programming is designed to fix by storing the results of these subproblems (a technique called memoization).
# Space Complexity: O(n)
# The space complexity is determined by the maximum depth of the recursion call stack, which is n in this case.