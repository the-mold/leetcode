from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        N = 9
        
        # State tracking: store used numbers for each row, col, and box
        rows_used = [set() for _ in range(N)]
        cols_used = [set() for _ in range(N)]
        boxes_used = [set() for _ in range(N)]

        # One-time pass to populate the initial state
        for r in range(N):
            for c in range(N):
                if board[r][c] != ".":
                    num = board[r][c]
                    box_index = (r // 3) * 3 + (c // 3)
                    
                    rows_used[r].add(num)
                    cols_used[c].add(num)
                    boxes_used[box_index].add(num)

        def backtrack(r, c):
            # If we've moved past the last column, go to the next row
            if c == N:
                c = 0
                r += 1
            
            # If we've filled all rows, we found a solution
            if r == N:
                return True

            # If the cell is already filled, move to the next one
            if board[r][c] != ".":
                return backtrack(r, c + 1)

            box_index = (r // 3) * 3 + (c // 3)
            
            # Try placing numbers 1-9
            for num_val in range(1, 10):
                num = str(num_val)
                
                # The O(1) validity check
                if (num not in rows_used[r] and
                    num not in cols_used[c] and
                    num not in boxes_used[box_index]):
                    
                    # Place the number
                    board[r][c] = num
                    rows_used[r].add(num)
                    cols_used[c].add(num)
                    boxes_used[box_index].add(num)

                    # Recurse
                    if backtrack(r, c + 1):
                        return True
                    
                    # Backtrack: remove the number
                    board[r][c] = "."
                    rows_used[r].remove(num)
                    cols_used[c].remove(num)
                    boxes_used[box_index].remove(num)
            
            # If no number worked, trigger backtracking from the previous call
            return False

        backtrack(0, 0)
