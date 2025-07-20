class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        self.perimeter = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or grid[r][c] == "X":
                return
            
            grid[r][c] = "X"

            # count sides
            # up
            if r == 0 or grid[r - 1][c] == 0:
                self.perimeter += 1
            # down
            if r == rows - 1 or grid[r + 1][c] == 0:
                self.perimeter += 1
            #left
            if c == 0 or grid[r][c - 1] == 0:
                self.perimeter += 1
            #right
            if c == cols - 1 or grid[r][c + 1] == 0:
                self.perimeter += 1

            # check for neighbours
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)

        return self.perimeter 

# T: O(n*m)
# S: O(n*m)