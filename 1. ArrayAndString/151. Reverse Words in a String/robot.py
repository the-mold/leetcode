def reverseWords(self, s: str) -> str:
  s_splitted = s.split()
  reversed_list = s_splitted[::-1]
  
  return " ".join(reversed_list)