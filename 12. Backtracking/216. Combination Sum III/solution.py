class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        numbers = [x for x in range(1, 10)]

        def backtracking(start_idx, current_combinations, remainder):
            if remainder < 0 or len(current_combinations) > k:
                return

            if remainder == 0 and len(current_combinations) == k:
                res.append(list(current_combinations))
                return

            for i in range(start_idx, len(numbers)):
                tested_number = numbers[i]
                current_combinations.append(tested_number)

                backtracking(i + 1, current_combinations, remainder - tested_number)

                current_combinations.pop()

        backtracking(0, [], n)

        return res
    

# Time Complexity
# The algorithm uses backtracking to find all combinations of k numbers from a fixed set of 9 numbers ([1, 2, ..., 9]). The work is done in the recursive backtracking function.

# Decision Tree: The algorithm explores a decision tree where each node represents a choice to include a number in the current combination. The depth of this tree is at most k, as we stop once a combination has k numbers.
# Number of Combinations: The problem is to choose k distinct numbers from a set of 9. The number of ways to do this is given by the binomial coefficient "9 choose k", or C(9, k).
# Work per Combination: For each valid combination found at a depth of k, we create a copy of the current_combinations list. This operation takes O(k) time.
# The total number of nodes in the decision tree is related to the number of possible combinations. The number of leaf nodes that represent valid solutions is C(9, k). The total number of operations is roughly proportional to the number of nodes in the tree multiplied by the work at each node.

# A loose upper bound on the number of recursive calls would be the total number of subsets, which is 2⁹. However, since the recursion depth is limited to k, a tighter bound is the number of combinations of size k from 9 elements, which is C(9, k).

# Therefore, the time complexity is approximately O(k * C(9, k)).

# Since k is at most 9, this is a constant-time complexity from an asymptotic perspective, but it's a useful expression for understanding the performance for different values of k. The maximum value of C(9, k) occurs at k=4 or k=5 (C(9, 4) = 126), so the number of operations is quite small.
# BUT!!!
# Since the set of numbers to choose from is fixed at 9 ([1, 2, ..., 9]), the number of possible combinations C(9, k) is bounded by a constant. The maximum value for C(9, k) is C(9, 4) = 126. Similarly, k is also bounded (it can't be greater than 9).

# In Big O notation, we are concerned with how an algorithm's runtime scales as its input grows towards infinity. Because the inputs k and n are constrained by the fixed set of 9 numbers, the total number of operations your algorithm performs will never exceed a certain fixed limit, regardless of the specific values of k and n.
# Therefore, in the strictest sense of asymptotic analysis, the time complexity can be simplified to:
# O(1)
# This means the algorithm runs in constant time.


# Space Complexity
# The space complexity is determined by the storage required for the recursion stack and the output list.

# Recursion Stack: The backtracking function is called recursively. The maximum depth of the recursion is k (the size of the combination). Therefore, the space used by the call stack is O(k).
# Output Storage: The res list stores all the valid combinations. In the worst case, this will be all C(9, k) combinations, each of size k. The space required for the output is O(k * C(9, k)).
# Auxiliary Space: The current_combinations list holds at most k elements, so it takes O(k) space.
# Combining these factors, the dominant term is the storage for the output. Thus, the overall space complexity is O(k * C(9, k)). If we exclude the space required for the output itself (as is common in complexity analysis), the space complexity would be O(k) due to the recursion depth.