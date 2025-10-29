class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        # memo stores the results for subproblems (i, j).
        memo = {}

        def solve(i: int, j: int) -> int:
            # Base Case 1: If word1 is exhausted, we must insert the rest of word2.
            if i == n1:
                return n2 - j
            
            # Base Case 2: If word2 is exhausted, we must delete the rest of word1.
            if j == n2:
                return n1 - i

            # Memoization: If we've solved this state, return the cached result.
            if (i, j) in memo:
                return memo[(i, j)]

            # --- Recursive Step ---

            # Case 1: Characters match, no operation needed.
            if word1[i] == word2[j]:
                result = solve(i + 1, j + 1)
            
            # Case 2: Characters do not match.
            else:
                # Find the minimum cost among the three possible operations.
                
                # Insert: insert_cost = 1 + solve(i, j + 1)
                # Meaning: Insert word2[j] into word1 at position i so they match at this spot.
                # Pointers: Keep i (we still need to match word1[i] next), advance j (we’ve matched word2[j] by insertion).
                # Intuition: Make word1 “catch up” to word2 by adding the missing char.
                insert_cost = 1 + solve(i, j + 1)
                
                # Delete: delete_cost = 1 + solve(i + 1, j)
                # Meaning: Delete word1[i] because it doesn’t match word2[j].
                # Pointers: Advance i (we removed word1[i]), keep j.
                # Intuition: Drop the bad char in word1 and try to match the next one.
                delete_cost = 1 + solve(i + 1, j)
                
                # Replace: replace_cost = 1 + solve(i + 1, j + 1)
                # Meaning: Replace word1[i] with word2[j], making them equal at this position.
                # Pointers: Advance both i and j (this position is now matched).
                # Intuition: Fix the mismatch directly, then move on.
                replace_cost = 1 + solve(i + 1, j + 1)
                
                result = min(insert_cost, delete_cost, replace_cost)
            
            # Cache the result before returning.
            memo[(i, j)] = result
            return result

        # Start the recursion from the beginning of both strings.
        return solve(0, 0)
