def mergeAlternately(self, word1, word2):
  output = []
  pointer = 0
  l1, l2 = len(word1), len(word2)

  while l1 > pointer and l2 > pointer:
    output.append(word1[pointer])
    output.append(word2[pointer])
    pointer += 1

  if l1 > pointer:
    output.append(word1[pointer:])

  if l2 > pointer:
    output.append(word2[pointer:])
  
  return output.join("")

#n = len(word1)
#m = len(word2)
# Time: O(n + m)
# Space: O(n + m)
