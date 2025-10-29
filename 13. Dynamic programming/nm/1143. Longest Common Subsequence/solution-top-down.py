class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # memo stores the results for subproblems (i, j) to avoid re-computation.
        # Key: (i, j), Value: LCS length for text1[i:] and text2[j:]
        memo = {}
        n1, n2 = len(text1), len(text2)

        def solve(i: int, j: int) -> int:
            # Base Case: If either pointer is out of bounds, we can't form a subsequence.
            if i >= n1 or j >= n2:
                return 0
            
            # Memoization: If we have already solved this subproblem, return the cached result.
            if (i, j) in memo:
                return memo[(i, j)]

            # --- Recursive Step ---

            # Case 1: The characters at the current pointers match.
            if text1[i] == text2[j]:
                # We found a common character. Add 1 to the result and
                # find the LCS for the rest of the strings.
                result = 1 + solve(i + 1, j + 1)
            
            # Case 2: The characters do not match.
            else:
                # We must skip a character. We explore both possibilities and
                # take the one that gives a longer subsequence.
                # Option A: Skip character in text1.
                # Option B: Skip character in text2.
                result = max(solve(i + 1, j), solve(i, j + 1))
            
            # Cache the result before returning.
            memo[(i, j)] = result
            return result

        # Start the recursion from the beginning of both strings.
        return solve(0, 0)
    
# Let:

# m be the length of text1.
# n be the length of text2.
# Time Complexity: O(m * n)
# Subproblems: The problem is broken down into subproblems defined by the state (i, j), which represents the LCS of text1[i:] and text2[j:].
# The index i can range from 0 to m.
# The index j can range from 0 to n.
# This gives a total of m * n unique subproblems (or states).
# Work per Subproblem: Thanks to memoization (the memo dictionary), the body of the solve(i, j) function is executed only once for each unique (i, j) pair.
# Inside the function, the work consists of a few comparisons, arithmetic operations, and at most two recursive calls.
# All these operations (character comparison, max() function, dictionary lookups and insertions) take constant time, O(1).
# Total Time: The total time complexity is the number of unique subproblems multiplied by the work done for each subproblem (excluding the recursive calls, which are handled by the memoization). Total Time = (Number of States) × (Work per State) Total Time = (m * n) × O(1) = O(m * n)
# Without memoization, the complexity would be exponential, as many subproblems would be recalculated repeatedly.

# Space Complexity: O(m * n)
# The space complexity is determined by two factors: the recursion stack depth and the size of the memoization table.

# Memoization Table (memo):
# The memo dictionary stores the result for every unique state (i, j).
# In the worst case, the algorithm will compute and store the result for all m * n states.
# Therefore, the space required for the memo dictionary is O(m * n).
# Recursion Stack:
# The depth of the recursion is determined by the longest path of recursive calls.
# In each step, either i or j (or both) is incremented.
# The maximum depth of the recursion stack will be m + n (e.g., in the case where characters never match, you might traverse all of one string and then all of the other).
# This contributes O(m + n) to the space complexity.
# Overall Space: The space required for the memoization table (O(m * n)) is the dominant factor compared to the recursion stack (O(m + n)).

# Therefore, the total space complexity is O(m * n).
    
    
    
# How it Solves Example 1: text1 = "abcde", text2 = "ace"
# solve(0, 0): text1[0] ('a') == text2[0] ('a').
# They match! The result is 1 + solve(1, 1).
# solve(1, 1): text1[1] ('b') != text2[1] ('c').
# They don't match. The result is max(solve(2, 1), solve(1, 2)).
# solve(2, 1): text1[2] ('c') == text2[1] ('c').
# They match! Result is 1 + solve(3, 2).
# solve(1, 2): text1[1] ('b') != text2[2] ('e').
# They don't match. Result is max(solve(2, 2), solve(1, 3)).
# ...and so on. The memoization ensures that if solve(3, 2) is needed by multiple paths, it's only computed once.

# Eventually, the base cases return 0, and the results bubble back up:

# solve(3, 2) (for "de" and "e") will become 1 + solve(4, 3) which is 1 + 0 = 1.
# solve(2, 1) becomes 1 + 1 = 2.
# The other branches are calculated similarly.
# Finally, solve(0, 0) gets its answer, which will be 3.