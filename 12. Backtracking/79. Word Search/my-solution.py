class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0]) 

        self.found = False
        def backtracking(idx, r, c):
            if self.found:
                return

            if idx == len(word):
                self.found = True
                return

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
                
            if word[idx] != board[r][c]:
                return

            # temporary mark the cell
            temp = board[r][c]
            board[r][c] = "#"
            
            backtracking(idx + 1, r + 1, c)
            backtracking(idx + 1, r - 1, c)
            backtracking(idx + 1, r, c + 1)
            backtracking(idx + 1, r, c - 1)

            board[r][c] = temp

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    backtracking(0, r, c)
                    if self.found:
                        return self.found

        return self.found

