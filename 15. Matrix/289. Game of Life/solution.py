import copy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        state = copy.deepcopy(board)

        def get_alive_neighbours(r, c):
            alive_neighbours = 0
            for row, col in [
                (r - 1, c),
                (r - 1, c + 1),
                (r, c + 1),
                (r + 1,c + 1),
                (r + 1,c),
                (r + 1,c - 1),
                (r,c - 1),
                (r - 1,c - 1)
            ]:
                if row < 0 or row >= rows or col < 0 or col >= cols:
                    continue
                alive_neighbours += state[row][col]
            
            return alive_neighbours

        for r in range(rows):
            for c in range(cols):
                if state[r][c] == 0:
                    # condition 4
                    if get_alive_neighbours(r, c) == 3:
                        board[r][c] = 1
                elif state[r][c] == 1:
                    alive_neighbours = get_alive_neighbours(r, c)
                    if alive_neighbours < 2 or alive_neighbours > 3:
                        board[r][c] = 0

# T:O(n*m)
# S:O(n*m)