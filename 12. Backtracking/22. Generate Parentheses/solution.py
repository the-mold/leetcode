from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generates all combinations of well-formed parentheses for n pairs.
        """
        result = []

        # The backtracking function will build the string.
        # It needs to track the number of open and close parentheses used.
        def backtrack(current_string: str, open_count: int, close_count: int):
            # Base Case: If the string has reached its maximum length (2 * n),
            # we have a complete and valid combination.
            if len(current_string) == 2 * n:
                result.append(current_string)
                return

            # --- Recursive Steps (Decisions) ---

            # Decision 1: Can we add an opening parenthesis?
            # We can if we haven't used all 'n' available open parentheses.
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)

            # Decision 2: Can we add a closing parenthesis?
            # We can if the number of closing parentheses is less than the number
            # of open ones. This is the key constraint for well-formedness.
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)

        # Start the backtracking process with an empty string and zero counts.
        backtrack("", 0, 0)
        return result


# Time Complexity: O( (4^N) / (N * sqrt(N)) )
# The time complexity is proportional to the number of valid sequences we generate. The number of valid sequences is the n-th Catalan number.
# For each valid sequence of length 2N, we do O(N) work to create the string.
# A loose upper bound for the Catalan numbers is 4^N. A tighter asymptotic bound is 
# (4^N) / (N * sqrt(N)).
# Therefore, the time complexity is dominated by the number of solutions we have to generate and build.

# Space Complexity: O(N) (excluding output) or O(N * C_n) (including output)
# Excluding the output array: The space is determined by the maximum depth of the recursion call stack. At any point, we are building a string of length up to 2N. The recursion depth is 2N. Therefore, the space complexity of the call stack is O(N).
# Including the output array: We need to store all C_n valid combinations, and each combination has a length of 2N. The space required for the result list is therefore O(N * C_n), which is asymptotically equivalent to O(N * (4^N) / (N * sqrt(N))). This is the dominant factor.
