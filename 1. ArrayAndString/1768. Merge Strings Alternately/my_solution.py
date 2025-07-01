def mergeAlternately(self, word1, word2):
  output = ""
  pointer = 0

  while len(word1) > pointer and len(word2) > pointer:        #O(n)
    output = f"{output}{word1[pointer]}{word2[pointer]}"      #O(n)
    pointer += 1

  if len(word1) > pointer:
    output = f"{output}{word1[pointer:]}"

  if len(word2) > pointer:
    output = f"{output}{word2[pointer:]}"            
  
  return output

#n = len(word1)
#m = len(word2)
# Time: O(n^2)
# Memory: O(n+m)
