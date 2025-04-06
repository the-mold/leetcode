def numberOfIslands(grid):
  rows = len(grid)
  cols = len(grid[0])

  def visit_neighbour_cells(r, c):
    if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
      return

    grid[r][c] = "0"
    # visit connected cells
    visit_neighbour_cells(r - 1, c) #Up
    visit_neighbour_cells(r + 1, c) #Down
    visit_neighbour_cells(r, c - 1) #Left
    visit_neighbour_cells(r, c + 1) #Right

  ans = 0
  for r in range(rows):
    for c in range(cols):
      if grid[r][c] == "1":
        ans += 1
        visit_neighbour_cells(r, c)
  
  return ans

#T: O(n*m)
#S: O(n*m)    , when there is a recursion involved, you count here number of stacked calls. In words case matrix has all 1s so you need to visit every cell, hence n*m.