def transpose(matrix):
  rows = len(matrix)
  cols = len(matrix[0])

  res = []
  for i in range(cols):
    res.append([0] * rows)

  for i in range(rows):
    for j in range(cols):
      res[j][i] = matrix[i][j]
  
  print("res", res)

  return res

# T: O(r * c)     # function itereates over all rows and columns, hence r * c.
# S: O(r * c)     # function itereates over all rows and columns, hence r * c.

transpose([[1,2,3],[4,5,6],[7,8,9]])
