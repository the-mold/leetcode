def count_letters_a(string, n):
  count = 0
  
  str_pointer = 0
  i = 0
  
  while i < n:
    if str_pointer >= len(string):
      str_pointer = 0
      
    if string[str_pointer].lower() == "a":
      count += 1
    

    str_pointer += 1
    i += 1
    
  return count

# T:O(n)
# S:O(1)


# count_letters_a("abcabcd", 10) #3
count_letters_a("abcabcd", 11) #4
