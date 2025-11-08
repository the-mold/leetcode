from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # memo[i] = (max_product_ending_at_i, min_product_ending_at_i)
        memo = {}

        def solve(i: int) -> tuple:
            """
            Returns (max_product, min_product) for subarray ending at index i.
            """
            # Base case: first element
            if i == 0:
                return (nums[0], nums[0])
            
            # Check cache
            if i in memo:
                return memo[i]

            # Get max and min from previous position
            prev_max, prev_min = solve(i - 1)
            
            current = nums[i]
            
            # Three candidates for both max and min:
            # 1. Start fresh from current element
            # 2. Extend previous max
            # 3. Extend previous min (important when current is negative)
            candidates = [current, current * prev_max, current * prev_min]
            
            current_max = max(candidates)
            current_min = min(candidates)
            
            # Cache and return
            memo[i] = (current_max, current_min)
            return memo[i]

        # The answer is the maximum of all max_products ending at any index
        result = float('-inf')
        for i in range(len(nums)):
            max_ending_here, _ = solve(i)
            result = max(result, max_ending_here)
            
        return result
      
      
# Time Complexity: O(n)
# The solve(i) function is called for each index from 0 to n-1.
# Due to memoization, each index is computed exactly once. Subsequent calls return the cached result in O(1).
# Inside each call, we do constant-time work: a few multiplications, comparisons, and dictionary operations.
# The final loop (in the first version) or the single call to solve(n-1) (in the alternative) also runs in O(n) total.

# Total: O(n)
# Space Complexity: O(n)
# Memo dictionary: Stores up to n entries, each holding a tuple (max, min) → O(n).
# Recursion call stack: The maximum depth is n (when calling solve(n-1) → solve(n-2) → ... → solve(0)) → O(n).
# Total auxiliary space: O(n) + O(n) = O(n).
