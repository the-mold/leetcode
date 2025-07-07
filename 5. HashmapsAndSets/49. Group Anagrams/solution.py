def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
  groups = {}

  for word in strs:
    
    key = "".join(sorted(word))

    if not key in groups:
      groups[key] = []
    
    groups[key].append(word)
  
  return list(groups.values())

#T:O(n * m log m), where m is maximum word length
#S:(n * m), case when each word is in own anagram group. We store for each word a key and word itself