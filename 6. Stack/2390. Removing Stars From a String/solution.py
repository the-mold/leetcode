def removeStars(s: str) -> str:
  res = []
  for ch in s:
      if ch == "*":
          res.pop()
      else:
          res.append(ch)
  
  return "".join(res)

#T:O(n)
#S:O(n)
