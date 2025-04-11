def exist(board, word):
  rows, cols = len(board), len(board[0])

  def dfs(r, c, index):
    if index == len(word):
      return True
    
    if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]:
      return False
    
    temp = board[r][c]
    board[r][c] = "#"

    found = dfs(r + 1, c, index + 1) or dfs(r - 1, c, index + 1) or dfs(r, c + 1, index + 1) or dfs(r, c - 1, index + 1)

    board[r][c] = temp

    return found


  for r in range(rows):
    for c in range(cols):
      if board[r][c] == word[0] and dfs(r, c, 0):
        return True
      
  return False

#T:O(n * m * 4^L)     words case when each word has 4 choises. L is the length of the word. n and m are matrix params.
#S:O(L) , recursion depth is equal to word length


print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
