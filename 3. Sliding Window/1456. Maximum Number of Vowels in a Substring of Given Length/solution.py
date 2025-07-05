def maxVowels(s: str, k: int) -> int:
  vowels = set('aeiou')
  count = 0
  for v in s[:k]:         #O(k)
      if v in vowels:
          count += 1
  
  max_count = count

  for i in range(k, len(s)):      #O(n-k)
      # gained one vowel when window slided
      if s[i] in vowels:
          count += 1
      
      # lost one vowel when window slided
      if s[i-k] in vowels:
          count -= 1

      max_count = max(max_count, count)
  
  return max_count

#T: O(k) + O(n - k) = O(n)
#S: O(1)
