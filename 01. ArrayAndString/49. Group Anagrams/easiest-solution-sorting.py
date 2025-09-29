class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      dict_w = {}
      for word in strs:
          word_sorted = "".join(sorted(word))
          dict_w.setdefault(word_sorted, []).append(word)
      
      res = []
      for key in dict_w:
          res.append(dict_w[key])

      return res

#T:O(n * k * log k)
#S:O(n*k)
