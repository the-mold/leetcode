class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def backtracking(str_list, left_count, right_count):
            if len(str_list) == 2 * n:
                ans.append("".join(str_list))
                return

            if left_count < n:
                str_list.append("(")
                backtracking(str_list, left_count + 1, right_count)
                str_list.pop()

            if right_count < left_count:
                str_list.append(")")
                backtracking(str_list, left_count, right_count + 1)
                str_list.pop()
        
        backtracking([], 0, 0)

        return ans
    
# Intuition
# See the screenshot. This is how the algorithm is performerd. First you explore the left part. When you reach the left bottom, you start removing elements from 
# `str_list` with .pop(). Then you come back to the case with "(" and move to the right part.

# Time Complexity: O( (4^N) / sqrt(N) )
# The algorithm visits exactly as many nodes as there are valid parentheses combinations, which grows exponentially but is constrained by the Catalan number formula.
# - What we're generating: All valid combinations of n pairs of parentheses
# - How many valid combinations exist: This is the nth Catalan number = 4^n / √n (approximately)


# Space Complexity: O(N) (excluding output) or O(N * C_n) (including output)
# Excluding the output array: The space is determined by the maximum depth of the recursion call stack. At any point, we are building a string of length up to 2N. The recursion depth is 2N. Therefore, the space complexity of the call stack is O(N).
# Including the output array: We need to store all C_n valid combinations, and each combination has a length of 2N. The space required for the result list is therefore O(N * C_n), which is asymptotically equivalent to O(N * (4^N) / (N * sqrt(N))). This is the dominant factor.
