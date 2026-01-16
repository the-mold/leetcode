def token_transform(s, tokens):
  return _token_transform(s, tokens, {})

def _token_transform(s, tokens, memo):
  if s in memo:
    return memo[s]
    
  if s == "":
    return ""
    
  i = 0
  j = 1

  res = ""
  while i < len(s):
    if s[i] == "$":
      while s[j] != "$":
        j += 1

      candidate = s[i:j+1]
      if candidate in tokens:
        parsed_string = _token_transform(tokens[candidate], tokens, memo)
        res += parsed_string

      i = j + 1
      j = i + 1
    else:
      res += s[i]
      i += 1
      j += 1

  memo[s] = res
  return memo[s]
  