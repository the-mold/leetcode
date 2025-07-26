from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations in candidates where the numbers sum to target.
        The same number may be chosen from candidates an unlimited number of times.
        """
        result = []
        
        def backtrack(start_index: int, current_combination: List[int], remaining_target: int):
            """
            A recursive helper function to find combinations.
            
            :param start_index: The index in `candidates` to start our search from.
                                This prevents duplicate combinations (e.g., [2,3] and [3,2]).
            :param current_combination: The list of numbers we've chosen so far.
            :param remaining_target: The remaining sum we need to achieve.
            """
            # Base Case 1: We've found a valid combination.
            if remaining_target == 0:
                # Append a copy of the combination to the result.
                result.append(list(current_combination))
                return

            # Base Case 2: We've overshot the target. Prune this path.
            if remaining_target < 0:
                return

            # --- Recursive Step ---
            # Iterate through the candidates, starting from the `start_index`.
            for i in range(start_index, len(candidates)):
                candidate = candidates[i]
                
                # 1. Choose the candidate
                current_combination.append(candidate)
                
                # 2. Explore further
                # We pass `i` as the next start_index (not `i + 1`) because
                # we are allowed to reuse the same number.
                backtrack(i, current_combination, remaining_target - candidate)
                
                # 3. Backtrack (un-choose the candidate)
                # This is crucial. We remove the last added number so we can explore
                # other possibilities in the loop.
                current_combination.pop()

        # Start the backtracking process from the beginning of the candidates list.
        backtrack(0, [], target)
        return result

# Complexity Analysis
# Let N be the number of candidates. Let T be the target value. Let M be the minimum value among the candidates.

# Time Complexity: O(N^(T/M))
# This is a rough upper bound, but it captures the exponential nature of the problem.

# The recursion tree can go as deep as T / M in the worst case (e.g., if the smallest candidate is 1 and the target is T, the longest combination has length T).
# At each step in the recursion, we iterate through up to N candidates.
# This creates a branching factor of N. The depth of the tree is roughly T/M. This leads to a time complexity that is approximately O(N^(T/M)). The actual number of nodes explored is less due to pruning, but this provides a general idea of the complexity.
# Space Complexity: O(T/M)
# This complexity primarily comes from the recursion call stack.
# The maximum depth of the recursion is the maximum length of a valid combination. In the worst case, this happens when we repeatedly use the smallest candidate (M) to reach the target (T). The depth would be T / M.
# Therefore, the space required for the call stack is O(T/M).
