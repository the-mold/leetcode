class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n

        memo = {
            # if i am at destination, then i found a valid path
            (rows-1, cols-1): 1
        }

        def solve(r, c):
            if (r,c) in memo:
                return memo[(r,c)]
            
            if r >= rows or c >= cols:
                return 0

            path_right = solve(r,c+1)
            path_down = solve(r+1,c)
            res = path_right + path_down

            memo[(r,c)] = res
            return res

        return solve(0, 0)

