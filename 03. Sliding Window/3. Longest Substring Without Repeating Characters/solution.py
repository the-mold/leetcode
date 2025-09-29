def lengthOfLongestSubstring(self, s):
  l = 0
  ans = 0
  sett = set()

  for r in range(len(s)):
    while s[r] in sett:
      sett.remove(s[l])
      l += 1
    
    ans = max(ans, r - l + 1)
    sett.add(s[r])
  
  return ans