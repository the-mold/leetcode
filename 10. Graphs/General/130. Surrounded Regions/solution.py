from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            """
            Performs a Depth-First Search to find all 'O's connected to the
            cell (r, c) and marks them as 'S' (Safe).
            """
            # Check boundaries and if the cell is an 'O'
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            
            # Mark the current cell as safe
            board[r][c] = 'S'
            
            # Recursively visit neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. Mark 'O's on the border and their connected regions as 'S'
        # Check first and last columns
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)

        # Check first and last rows
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)

        # 2. Flip remaining 'O's to 'X's and 'S's back to 'O's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    # This 'O' is surrounded, capture it
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    # This was a safe 'O', restore it
                    board[r][c] = 'O'

# Intuition
# Instead of finding good surrounded cells, find all the bad ones and mark them with "S" for safe. You assume that all other cells are good and could be flipped to X.

# The key insight is that any region of 'O's connected to the border of the board is not surrounded and should not be captured. All other 'O's are surrounded and should be flipped to 'X's.

# Here is the plan to solve this problem:

# Identify Unflippable 'O's: We'll start by iterating through the cells on the four borders of the board. If we find an 'O', we know it's part of a region that cannot be captured.
# Mark Unflippable Regions: From each border 'O', we'll perform a Depth-First Search (DFS) to find all connected 'O's. We'll temporarily mark these 'O's (e.g., changing them to 'S' for 'Safe') to signify they shouldn't be flipped.
# Capture Surrounded 'O's: After marking all the "safe" regions, we'll iterate through the entire board. Any cell that is still an 'O' is not connected to the border and is therefore surrounded. We'll flip these 'O's to 'X's.
# Restore Unflippable 'O's: Finally, we'll do one last pass to change our temporary 'S' markers back to 'O's.


#Complexity
# Time Complexity: O(m * n)
# The overall time complexity is determined by the number of times we visit each cell in the grid.

# DFS from Borders: We start a Depth-First Search (DFS) from each 'O' on the four borders of the grid. The key insight here is that each cell is visited by the dfs function at most once. When dfs visits a cell (r, c), it immediately marks it as 'S'. Any future dfs call on that same cell will see that it's no longer an 'O' and will return immediately. Therefore, the total work done by all the DFS calls combined is proportional to the total number of cells, which is O(m * n).
# Final Grid Traversal: After the DFS phase, we iterate through every cell of the grid one last time to flip the remaining 'O's to 'X's and the 'S's back to 'O's. This is a nested loop that runs m * n times, so it's also O(m * n).
# Combining these steps, the total time complexity is O(m * n) + O(m * n), which simplifies to O(m * n).

# Space Complexity: O(m * n)
# The space complexity is determined by the extra memory used by the algorithm, not including the input board itself.

# Recursion Stack: The primary consumer of extra space is the recursion stack used by the dfs function. In the worst-case scenario, you could have a grid where a path of 'O's snakes through every single cell (e.g., a spiral shape). In this case, the recursion could go m * n levels deep before it starts to unwind.
# Therefore, the space complexity is O(m * n) to account for the maximum depth of the recursion stack.

# In summary:

# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
