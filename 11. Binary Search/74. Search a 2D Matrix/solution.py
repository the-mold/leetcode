class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, rows * cols - 1

        while l <= r:
            mid = (l + r) // 2
            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] >= target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
    
# Time Complexity: O(log(m * n))
# The algorithm performs a binary search on a virtual 1D array of size m × n (where m is the number of rows and n is the number of columns)
# Each iteration of the binary search reduces the search space by half
# The maximum number of iterations needed is log₂(m × n)
# Each iteration performs constant-time operations (calculating indices and comparing values)
# This meets the requirement specified in the problem statement to have a solution with O(log(m * n)) time complexity.

# Space Complexity: O(1)
# The algorithm uses only a constant amount of extra space regardless of input size
# It only stores a few variables (l, r, mid, row, col) regardless of how large the matrix is
# No additional data structures are created that scale with input size