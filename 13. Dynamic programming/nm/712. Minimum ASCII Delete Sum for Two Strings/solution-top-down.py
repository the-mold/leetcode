# Intuition: find the longest common subsequence es in problem 1143. Then perform simple operations to get ascii sum of deleted chars.

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)
        memo = {}

        def solve_max_common_sum(i: int, j: int) -> int:
            """
            Calculates the maximum ASCII sum of a common subsequence
            for s1[i:] and s2[j:].
            """
            # Base Case: If either pointer is out of bounds, no more common chars.
            if i >= n1 or j >= n2:
                return 0
            
            # Memoization: Return cached result if available.
            if (i, j) in memo:
                return memo[(i, j)]

            # --- Recursive Step ---

            # Case 1: Characters match.
            if s1[i] == s2[j]:
                # This character is part of the optimal subsequence.
                # Add its ASCII value and solve for the rest of the strings.
                result = ord(s1[i]) + solve_max_common_sum(i + 1, j + 1)
            
            # Case 2: Characters do not match.
            else:
                # We must skip a character. Take the path that maximizes the sum.
                # Option A: Skip character in s1.
                # Option B: Skip character in s2.
                result = max(
                    solve_max_common_sum(i + 1, j),
                    solve_max_common_sum(i, j + 1)
                )
            
            # Cache the result before returning.
            memo[(i, j)] = result
            return result

        # 1. Find the maximum ASCII sum of the common subsequence.
        max_common_sum = solve_max_common_sum(0, 0)
        
        # 2. Calculate the total ASCII sum of both original strings.
        total_sum = sum(ord(char) for char in s1) + sum(ord(char) for char in s2)
        
        # 3. The minimum delete sum is the total sum minus the sum of the
        #    characters we kept (from both strings).
        return total_sum - 2 * max_common_sum
