class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(numRows):
            row = [1]

            if i > 0:
                prev_row = res[i-1]

                for j in range(1, i):
                    row.append(prev_row[j-1]+prev_row[j])

                row.append(1)
            
            res.append(row)
        
        return res

# Time Complexity: O(n²)
# The outer loop runs numRows times (let's call this n)
# For each row i (from 0 to n-1), we perform i-1 operations to fill in the middle elements
# The total number of operations is approximately: 0 + 1 + 2 + ... + (n-1) = n(n-1)/2
# This sum equals n²/2 - n/2
# In Big O notation, we drop lower order terms and constants, resulting in O(n²)
# Simply put, as the input size n grows, the number of operations grows quadratically because we need to calculate more elements for each new row, and we're adding more rows.

# Space Complexity: O(n²)
# The space required is the total number of elements in the triangle
# The triangle has 1 element in the first row, 2 in the second, and so on up to n elements in the nth row
# The total number of elements is: 1 + 2 + 3 + ... + n = n(n+1)/2
# This equals n²/2 + n/2
# In Big O notation, this simplifies to O(n²)