class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        # check if player has won after the move
        #1. Check rows
        if self.checkRow(row, player):
            return player

        #2. Check cols
        if self.checkCol(col, player):
            return player

        #3. Check diagonal(top left to bottom right)
        if self.checkDiagonal(player):
            return player

        #4. Check anti diagonal(bottom left to top right)
        if self.checkAntidiagonal(player):
            return player

        return 0


    def checkRow(self, row, player):
        for c in range(len(self.board)):
            if self.board[row][c] != player:
                return False
        return True
    
    def checkCol(self, col, player):
        for r in range(len(self.board)):
            if self.board[r][col] != player:
                return False
        return True
    
    def checkDiagonal(self, player):
        for row in range(len(self.board)):
            if self.board[row][row] != player:      # we check only self.board[row][row] because in diagonal, all cells have the same coordinates, eg. (0,0), (1,1) etc
                return False
        return True

    def checkAntidiagonal(self, player):
        for row in range(len(self.board)):
            if self.board[row][self.n - row - 1] != player:
                return False
        return True


# Complexity Analysis
# Time Complexity: O(n), as for every move we are iterating over n cells 4 times to check for each of the column, row, diagonal row, and anti-diagonal. This gives us time complexity of O(4⋅n) which is equivalent to O(n).
# Space Complexity: O(n**2), as we are using 2-dimensional array board of size n * n.
