class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        used = [False] * n

        def backtrack(curr_arr):
            if len(curr_arr) == n:
                res.append(list(curr_arr))
                return

            for i in range(0, n):
                if used[i]:
                    continue

                used[i] = True
                curr_arr.append(nums[i])
                backtrack(curr_arr)
                curr_arr.pop()
                used[i] = False

        backtrack([])

        return res

# Time Complexity: O(n * n!)
# n! permutations: The fundamental reason for the complexity is that there are n! (n factorial) possible permutations for a list of n unique elements. The algorithm must generate every single one.
# O(n) work per permutation: When a valid permutation of length n is found (the base case len(curr_arr) == n), the line res.append(list(curr_arr)) creates a full copy of the curr_arr. This copy operation takes O(n) time.
# Total Time: The work to copy all n! permutations dominates the calculation. Therefore, the total time complexity is n! * O(n), which simplifies to O(n * n!).
# The work done in the intermediate recursive calls (the for loop) is also significant but leads to the same overall complexity. The number of nodes in the recursion tree is a sum related to n! (Σ P(n, k) from k=0 to n), and each node does some work, but the O(n) copy at each of the n! leaves is the most straightforward way to see the final complexity.

# Space Complexity: O(n)
# This refers to the extra space used by the algorithm, not including the space required to store the final output res.

# Recursion Depth: The maximum depth of the recursion tree is n. For example, to build the permutation [1, 2, 3], backtrack calls itself 3 times before hitting the base case. Each call adds a frame to the call stack. This contributes O(n) space.
# curr_arr: The temporary list curr_arr holds the permutation being built. Its maximum size is n. This is another O(n).
# used array: The used boolean array has a size of n, contributing O(n).
# Since these are all additive (O(n) + O(n) + O(n)), the total auxiliary space complexity is O(n).

# If you were to include the output list res in the space complexity calculation, it would be O(n * n!) because it stores n! permutations, each of length n. However, it's standard practice in algorithm analysis to exclude the space for the final result.