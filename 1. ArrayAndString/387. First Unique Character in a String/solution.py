def firstUniqChar(s: str) -> int:
  chars = {}

  for char in s:
    if char not in chars:
      chars[char] = 1
    else:
      chars[char] +=1

  for idx, char in enumerate(s):
    if char == 1:
      return idx
  
  return -1

#T:O(n)
#S:O(n)