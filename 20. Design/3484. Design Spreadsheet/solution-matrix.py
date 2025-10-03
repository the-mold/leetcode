ORD_A_LETTER = 65

class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = [[0 for i in range(26)] for _ in range(rows)]
        
    def column_letter_to_idx(self, letter):
        return ord(letter.upper()) - ORD_A_LETTER

    def setCell(self, cell: str, value: int) -> None:
        row, col = self.get_position(cell)
        self.grid[row][col] = value

    def resetCell(self, cell: str) -> None:
        row, col = self.get_position(cell)
        self.grid[row][col] = 0
    
    def get_position(self, cell):
        col = self.column_letter_to_idx(cell[0])
        row = int(cell[1:]) - 1
        return row, col
    
    def _get_cell_value(self, cell: str) -> int:
        if cell[0].isalpha():
            row, col = self.get_position(cell)
            return self.grid[row][col]
        else:
            return int(cell)

    def getValue(self, formula: str) -> int:
        formula = formula.replace("=", "")
        components = formula.split("+")

        return self._get_cell_value(components[0]) + self._get_cell_value(components[1])


# Let rows denote the number of rows in the spreadsheet, and let C=26 denote the number of columns.

# Time complexity: Initializing the table takes O(C×rows) time, since we must allocate a 2D array of size rows×26. Other operations take O(1) time, since they involve only string parsing and cell lookup.

# Space complexity: O(C×rows). Create a two-dimensional array with rows rows and 26 columns, requiring space of O(C×rows).