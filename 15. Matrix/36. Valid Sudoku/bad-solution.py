class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        #1. check rows
        for r in range(rows):
            sset = set()
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                val = board[r][c]
                if val in sset:
                    return False
                sset.add(val)

        # 2. check cols
        for c in range(cols):
            sset = set()
            for r in range(rows):
                if board[r][c] == ".":
                    continue
                val = board[r][c]
                if val in sset:
                    return False
                sset.add(val)

        # 3. check sub-boxes
        left_offset = 0
        top_offset = 0
        while top_offset < rows: 
            sset = set()
            for r in range(top_offset, top_offset + 3):
                for c in range(left_offset, left_offset + 3):
                    if board[r][c] == ".":
                        continue
                    val = board[r][c]
                    if val in sset:
                        return False
                    sset.add(val)

            left_offset += 3
            if left_offset >= cols:
                left_offset = 0
                top_offset += 3

        return True