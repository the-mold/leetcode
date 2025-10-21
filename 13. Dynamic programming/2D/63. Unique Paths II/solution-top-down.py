class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        # edge case: cannot reach finish because of obstacle
        if obstacleGrid[rows-1][cols-1] == 1:
            return 0

        memo = {
            # if i reach destination, this is one valid path
            (rows-1,cols-1): 1
        }

        def solve(r,c):
            if (r,c) in memo:
                return memo[(r,c)]

            if r >= rows or c >= cols:
                return 0

            # it is not a valid path if you hit the block
            if obstacleGrid[r][c] == 1:
                return 0

            right_paths = solve(r, c+1)
            bottom_paths = solve(r+1,c)

            res = right_paths + bottom_paths
            memo[(r,c)] = res

            return res
        
        return solve(0,0)

#T:O(nm)
#S:O(nm)