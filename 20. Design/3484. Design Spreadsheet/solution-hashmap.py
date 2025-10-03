class Spreadsheet:

    def __init__(self, rows: int):
        self.cell_values = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cell_values[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.cell_values:
            del self.cell_values[cell]

    def getValue(self, formula: str) -> int:
        i = formula.find("+")
        cell1 = formula[1:i]
        cell2 = formula[i + 1 :]
        val1 = (
            self.cell_values.get(cell1, 0) if cell1[0].isalpha() else int(cell1)
        )
        val2 = (
            self.cell_values.get(cell2, 0) if cell2[0].isalpha() else int(cell2)
        )
        return val1 + val2
      
# Let cellsCount denote the number of non-zero cells, which depends on how many times setCell is called.

# Time complexity: All operations run in O(1) time, since they involve only hash table lookups/updates and string parsing.

# Space complexity: O(cellsCount), as the hash table stores only non-zero cells.