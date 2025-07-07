def uniqueOccurrences(self, arr: List[int]) -> bool:
  freq = {}
  for num in arr:
      freq[num] = freq.get(num, 0) + 1
  
  seen = {}
  for count in freq.values():
      if count in seen:
          return False
      seen[count] = True
  
  return True

#T:O(2n) => O(n)
#S:O(2n) => O(n)