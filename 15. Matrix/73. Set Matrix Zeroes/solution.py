class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        rows_set, cols_set = set(), set()

        # mark all rows and cols that have zeros in them
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rows_set.add(r)
                    cols_set.add(c)
        
        # go through matrix again and change its cells
        for r in range(rows):
            for c in range(cols):
                if r in rows_set:
                    matrix[r][c] = 0
                elif c in cols_set:
                    matrix[r][c] = 0
        
# T:O(n*m)
#S: O(n*m)