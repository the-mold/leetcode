class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        def helper(r, c, direction):
            if r >= rows or r < 0 or c >= cols or c < 0 or matrix[r][c] == 0:
                return
            
            matrix[r][c] = "#"

            if direction == "top":
                # top
                helper(r - 1, c, direction)
            if direction == "bottom":
                # bot
                helper(r + 1, c, direction)
            if direction == "left":
                #left
                helper(r, c - 1, direction)
            if direction == "right":
                #right
                helper(r, c + 1, direction)

        # temporarily replace all 0s with hashtags
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[r][c] = "#"
                    # replace all numbers in each direction with hashtags
                    helper(r, c, "top")
                    helper(r, c, "bottom")
                    helper(r, c, "left")
                    helper(r, c, "right")

        # now replace all hashtags with 0s
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "#":
                    matrix[r][c] = 0

        return matrix
        