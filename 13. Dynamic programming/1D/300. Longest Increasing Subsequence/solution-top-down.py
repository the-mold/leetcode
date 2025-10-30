from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # memo stores results for subproblems (i, prev_i).
        # We use prev_i + 1 as the key to handle the initial case where prev_i is -1.
        memo = {}

        def solve(i: int, prev_i: int) -> int:
            # Base Case: If we've processed all elements, we can't extend the subsequence.
            if i == n:
                return 0
            
            # Memoization: If we've solved this state before, return the cached result.
            if (i, prev_i) in memo:
                return memo[(i, prev_i)]

            # --- Recursive Step: Make a decision for nums[i] ---

            # Choice 1: Skip nums[i].
            # The length is the LIS from the next element, keeping the same previous element.
            len_if_skipped = solve(i + 1, prev_i)

            # Choice 2: Include nums[i].
            # This is only possible if it's the first element (prev_i == -1) or
            # if nums[i] is strictly greater than the previous element included.
            len_if_included = 0
            if prev_i == -1 or nums[i] > nums[prev_i]:
                len_if_included = 1 + solve(i + 1, i)
            
            # The result for this state is the best of the two choices.
            result = max(len_if_included, len_if_skipped)
            
            # Cache the result before returning.
            memo[(i, prev_i)] = result
            return result

        # Start the recursion from the first element (index 0), with no previous element (-1).
        return solve(0, -1)
      
      
# Complexity Analysis
# Let n be the number of elements in the nums array.

# Time Complexity: O(n^2)
# State Space: The problem is broken down into subproblems defined by the state (i, prev_i).
# The index i (current element) can range from 0 to n.
# The index prev_i (previous element) can range from -1 to n-1.
# This gives a total of n * (n + 1) or roughly n^2 unique states.
# Work per State: Thanks to memoization, the body of the solve function is executed only once for each unique state (i, prev_i). The work inside the function (comparisons, max function, dictionary access) is constant time, O(1).
# Total Time: The total time complexity is the number of unique states multiplied by the work per state. Total Time = (Number of States) × (Work per State) = O(n^2) * O(1) = O(n^2).
# Space Complexity: O(n^2)
# The space complexity is determined by the size of the memoization table and the depth of the recursion stack.

# Memoization Table (memo):
# The memo dictionary stores the result for every unique state (i, prev_i).
# In the worst case, the algorithm will compute and store the result for all O(n^2) states.
# Therefore, the space required for the memo dictionary is O(n^2).
# Recursion Stack:
# The depth of the recursion is determined by the longest path of recursive calls. In each step, i is incremented by 1.
# The maximum depth of the recursion stack will be n.
# This contributes O(n) to the space complexity.
# The space for the memoization table (O(n^2)) dominates the space for the recursion stack (O(n)).

# Therefore, the total space complexity is O(n^2).