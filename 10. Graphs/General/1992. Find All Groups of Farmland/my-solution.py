class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows = len(land)
        cols = len(land[0])

        self.max_end_row = 0
        self.max_end_col = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or land[r][c] == 0:
                return 
            
            land[r][c] = 0

            self.max_end_row = max(self.max_end_row, r)
            self.max_end_col = max(self.max_end_col, c)

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        res = []
        for r in range(rows):
            for c in range(cols):
                if land[r][c] == 1:
                    self.max_end_row = r
                    self.max_end_col = c
                    dfs(r, c)
                    res.append([r, c, self.max_end_row, self.max_end_col])

        return res
