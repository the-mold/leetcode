def longestCommonPrefix(strs):
  if len(strs) == 0:
      return ""

  if len(strs) == 1:
      return strs[0]

  last_common_index = find_last_common_index(strs)

  first_str = strs[0]
  # print("last_common_index", last_common_index)
  res = first_str[:last_common_index + 1]
  print("res", res)

  return res

def find_last_common_index(strs):
  longest_possible_prefix = len(strs[0])
  i = 0
  while i < longest_possible_prefix:
    tested_letter = strs[0][i]
    for word in strs:
      # if next word has no such index
      if len(word) - 1 < i:
         return i - 1
      if word[i] != tested_letter:
        # print("returning for ", word[i], " and tested_letter:", tested_letter)
        return i - 1
    i += 1
  
  # print("-------went all the way")
  return i

longestCommonPrefix(["flower", "flow", "flight"])
longestCommonPrefix(["dog","racecar","car"])
longestCommonPrefix(["ab", "a"])
