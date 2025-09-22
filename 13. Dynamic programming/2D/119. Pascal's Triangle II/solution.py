class Solution:
    # initially, the cache is empty
    cache = {}

    # Internal helper function to calculate the number of ways
    def getNum(self, row, col):
        # store the position as a tuple, which will be used as a key in the cache
        rowCol = (row, col)
        # if the key is already in the cache, then return the cached value
        if rowCol in self.cache:
            return self.cache[rowCol]
        # if the row or column is 0, or if the row and column are the same, then there is only one way
        if row == 0 or col == 0 or row == col:
            self.cache[rowCol] = 1
            return 1
        # otherwise, the number of ways is the sum of the number of ways from the cell above and the cell to the left
        self.cache[rowCol] = self.getNum(row - 1, col - 1) + self.getNum(
            row - 1, col
        )
        return self.cache[rowCol]

    # Function to return the row of Pascal's Triangle
    def getRow(self, rowIndex):
        ans = []
        for i in range(rowIndex + 1):
            ans.append(self.getNum(rowIndex, i))
        return ans