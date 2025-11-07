class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtracking(current_numbers, start_idx):
            if len(current_numbers) == k:
                ans.append(list(current_numbers))
                return

            for i in range(start_idx, n + 1):
                current_numbers.append(i)
                backtracking(current_numbers, i+1)
                current_numbers.pop()

        backtracking([], 1)

        return ans

# Time Complexity: O(C(n, k) * k)
# - C(n, k) Combinations: The core of the problem is to find all possible combinations of k numbers from a set of n. The number of such combinations is given by the binomial coefficient "n choose k", which is mathematically written as C(n, k) or (n k). Your backtracking algorithm will have exactly C(n, k) leaf nodes in its recursion tree, each corresponding to one valid combination.
# - O(k) Work per Combination: When the base case is met (len(current_numbers) == k), you execute ans.append(list(current_numbers)). Creating a copy of current_numbers takes O(k) time because the list has k elements.
# - Total Time: The total time complexity is the number of valid combinations multiplied by the time it takes to process each one.
    # - Total Time = C(n, k) (number of solutions) * O(k) (time to copy each solution) = O(C(n, k) * k).
#The work done in the intermediate recursive calls (the for loops and append/pop operations) is also a factor, but it is accounted for within this overall complexity bound.

# Space Complexity: O(k)
# This complexity refers to the auxiliary space used by the algorithm, not including the space required to store the final ans list.
# - Recursion Depth: The backtracking function calls itself recursively. The maximum depth of this recursion will be k, because the function stops once the current_numbers list reaches a length of k. Each recursive call adds a frame to the call stack. This contributes O(k) to the space complexity.
# - current_numbers List: The current_numbers list stores the combination being built. Its maximum size is also k. This contributes another O(k).
# - Total Space: Since O(k) + O(k) is O(k), the total auxiliary space complexity is O(k).



# Combinations vs Permutations vs Choices with Replacement
# People often compare C(n, k) to n^k or P(n, k). Let's clarify:

# 1. C(n, k) (Combinations):
# What it is: Choosing k items from n, order doesn't matter.
# Analogy: Picking 3 toppings for a pizza from a list of 10.
# Complexity Growth: It grows and then shrinks. For a fixed n, C(n, k) is largest when k is close to n/2. For example, C(10, 1) is small, C(10, 5) is large, and C(10, 9) is small again.

# 2. P(n, k) (Permutations):
# What it is: Choosing and arranging k items from n, order matters.
# Formula: n! / (n - k)!
# Analogy: Awarding gold, silver, and bronze medals to 3 winners from 10 racers.
# Result: P(n, k) is always greater than or equal to C(n, k).

# 3. n^k (Choices with Replacement):
# What it is: Making k choices from n options, where you can re-use an option.
# Analogy: A 3-digit lock where each digit can be 0-9 (10^3 possibilities). You can have "333".
# Complexity Growth: This grows much faster than C(n, k).
