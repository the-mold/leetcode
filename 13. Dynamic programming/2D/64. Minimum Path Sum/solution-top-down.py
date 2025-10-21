class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        memo = {
            # base case. The cost the the bottom right cell is known and stays the same
            (rows - 1, cols - 1): grid[rows - 1][cols - 1]
        }

        def solve(r, c):
            if (r, c) in memo:
                return memo[(r,c)]

            # if you leave the grid
            if r >= rows or c >= cols:
                return float("inf")

            # check min cost for both right and bottom path
            right_path = solve(r, c+1)
            bottom_path = solve(r + 1, c)

            # The result is the current cell's value + the best of the two paths.
            res = grid[r][c] + min(right_path, bottom_path)

            memo[(r,c)] = res
            return res

        return solve(0, 0)
      
#T:O(n*m)
#S:O(n*m)