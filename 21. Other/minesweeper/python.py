def minesweeper(mines: list[str]):
  matrix = []
  for r in mines:
    matrix.append(list(r))

  rows = len(matrix)
  cols = len(matrix[0])

  for r in range(rows):
    for c in range(cols):
      if matrix[r][c] == "O":
        count = 0
        
        for r_change, c_change in [
          # top
          (-1, -1),
          (-1, 0),
          (-1, 1),
          # middle
          (0, -1),
          (0, 1),
          # bottom
          (1, -1),
          (1, 0),
          (1, 1),
        ]:
          r_check = r + r_change
          c_check = c + c_change

          if r_check < 0 or r_check >= rows or c_check < 0 or c_check >= cols:
            continue

          if matrix[r_check][c_check] == "X":
            count += 1
        
        matrix[r][c] = str(count)
  
  res = []
  for row in matrix:
    res.append(" ".join(row))

  return res





minesweeper(['XOO', 'OOO', 'XXO'])