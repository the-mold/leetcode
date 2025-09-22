class Solution:
    def getNum(self, row, col):
        if row == 0 or col == 0 or row == col:
            return 1
        return self.getNum(row-1,col-1) + self.getNum(row-1, col)
    
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        for i in range(rowIndex + 1):
            ans.append(self.getNum(rowIndex, i))
        
        return ans