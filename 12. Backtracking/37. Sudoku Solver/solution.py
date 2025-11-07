class Solution:
    def is_valid(self, num, rows, cols, r, c, board):
        # check row
        for check_c in range(cols):
            if board[r][check_c] == num:
                return False

        # check col
        for check_r in range(rows):
            if board[check_r][c] == num:
                return False

        # check box
        start_r = (r // 3) * 3
        end_r = start_r + 3
        start_c = (c // 3) * 3
        end_c = start_c + 3
        for check_r in range(start_r, end_r):
            for check_c in range(start_c, end_c):
                if board[check_r][check_c] == num:
                    return False

        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ".":
                    for num in range(1, 10):
                        num_char = str(num)
                        if self.is_valid(num_char, rows, cols, r, c, board):
                            board[r][c] = str(num_char)
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[r][c] = "."
                    
                    return False
        
        return True
      
#T:O(9**M), where M is number of empty cells. In worst case we need to try all 9 numbers
#S:O(M)