class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def found_word(r, c, str_idx):
            letter = word[str_idx]
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != letter or visited[r][c]:
                return False

            visited[r][c] = True

            new_idx = str_idx + 1
            if new_idx == len(word):
                return True

            is_found = found_word(r + 1, c, new_idx) or found_word(r - 1, c, new_idx) or found_word(r, c + 1, new_idx) or found_word(r, c - 1, new_idx)

            # revert the change, a clean slate and no side-effect
            visited[r][c] = False

            return is_found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if found_word(r, c, 0):
                        return True

        return False

# ⏱️ Time Complexity: O(m × n × 4^L)
# Where:

# m = number of rows
# n = number of columns
# L = length of the word
# Breakdown:
# Outer loops: O(m × n) - try starting from each cell
# DFS from each starting cell: O(4^L) in worst case
# Total: O(m × n × 4^L)
# Why 4^L?
# At each step of the DFS:

# We have 4 directions to explore (up, down, left, right)
# We do this for L steps (length of word)
# Worst case: 4 × 4 × 4 × ... (L times) = 4^L
# However, the visited array provides pruning, so in practice it's much better than 4^L.

# 💾 Space Complexity: O(L)
# Space Usage:
# Visited array: O(m × n) - but this is input modification, not extra space
# Recursion stack: O(L) - maximum depth is word length
# Total: O(L) if we modify input, O(m × n + L) if we use separate visited array
# 🎯 Practical Analysis
# Best Case: O(m × n)
# Word found immediately at first position
# No backtracking needed
# Average Case: Much better than O(m × n × 4^L)
# Visited array prevents revisiting cells
# Most paths terminate early due to character mismatches
# Effective branching factor << 4
# Worst Case: O(m × n × 4^L)
# Word uses all unique characters
# Many valid partial paths exist
# Example: Finding "ABCDEFGH" in a grid full of these letters