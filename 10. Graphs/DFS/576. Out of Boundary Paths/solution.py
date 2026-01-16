class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        ans = self._breaking_boundaries(m, n, maxMove, startRow, startColumn, {})
        return ans % MOD

    def _breaking_boundaries(self, rows, cols, k, r, c, memo):
        key = (k, r, c)
        if key in memo:
            return memo[key]
        
        if k < 0:
            return 0
        
        r_inbounds = 0 <= r < rows
        c_inbounds = 0 <= c < cols
        if not r_inbounds or not c_inbounds:
            return 1

        total = 0
        opt = [
            (-1, 0),
            (0, 1),
            (1,0),
            (0,-1)
        ]
        for dr, dc in opt:
            total += self._breaking_boundaries(rows, cols, k - 1, r + dr, c + dc, memo)

        memo[key] = total
        return memo[key]

# Without memo:
#T: 4**k

# With memo:
#m = max number of rows
#n = max number of cols
# T:O(mnk)
# S:O(mnk)