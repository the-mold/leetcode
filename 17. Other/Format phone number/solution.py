def format_numer(string):
  n = 0
  for i in range(len(string)):
    if string[i].isnumeric():
      n += 1
  
  ans = ""
  segment_pointer = 1
  numbers_left = n
  
  for i in range(len(string)):
    if string[i].isnumeric():
      if numbers_left == 2 and segment_pointer == 3:
        ans += "-"
        segment_pointer = 1
      elif segment_pointer == 4:
        ans += "-"
        segment_pointer = 1
      
      ans += string[i]
      
      segment_pointer += 1
      numbers_left -= 1
  
  return ans

#format_numer('00-44 48 5555 8361') #004-448-555-583-61
# format_numer('0 - 22 1985--324')

# XXX-XXX-XX
# XXX-XX-XX
