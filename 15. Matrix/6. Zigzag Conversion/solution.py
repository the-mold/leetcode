class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows == len(s):
            return s

        matrix = [[] for _ in range(numRows)]

        current_row = 0
        current_step = 1
        for i in range(len(s)):
            matrix[current_row].append(s[i])

            if current_row == numRows - 1:
                current_step = -1
            if current_row == 0:
                current_step = 1
            
            current_row += current_step

        ans = ""
        for row in range(len(matrix)):
            ans += "".join(matrix[row])
        
        return ans
      
#T:O(n)
#S:O(n)


# Intuition:
# Fill up matrix of `numRows` rows from top to bottom and then from bottom to top to get a zigzag representation.
