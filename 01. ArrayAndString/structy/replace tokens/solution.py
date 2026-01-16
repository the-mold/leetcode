def token_replace(s, tokens):
  i = 0
  j = 1

  res = []
  while i < len(s):
    if s[i] == "$":
      while s[j] != "$":
        j += 1

      candidate = s[i:j+1]
      if candidate in tokens:
        res.append(tokens[candidate]) 

      i = j + 1
      j = i + 1
    else:
      res.append(s[i])
      i += 1
      j += 1

  return "".join(res)

# T:O(n)
# S:O(n)
