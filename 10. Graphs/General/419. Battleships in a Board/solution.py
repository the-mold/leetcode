class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == ".":
                return
            
            board[r][c] = "."
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        res = 0
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X":
                    res += 1
                    dfs(r, c)
        
        return res
    
#T: O(n * m)
#S: O(n * m)
