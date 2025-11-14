class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345

        rows = len(grid)
        cols = len(grid[0])

        ans = [[1] * cols for _ in range(rows)]
        prefix = 1
        # left to right
        for r in range(rows):
            for c in range(cols):
                ans[r][c] = prefix 
                prefix = (prefix * grid[r][c]) % MOD 

        # right to left
        suffix = 1
        for r in range(rows-1, -1, -1):
            for c in range(cols-1,-1,-1):
                ans[r][c] = (ans[r][c] * suffix) % MOD
                suffix = (suffix * grid[r][c]) % MOD 
        
        return ans
    
# T:O(n)
# S:O(1)
