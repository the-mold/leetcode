
def expand(s):
  if len(s) == 0:
    return [""]
  
  res = []
  choices, remainder = get_choices(s)
  remaining_choices = expand(remainder)
  for choice in choices:
    for rc in remaining_choices:
      res.append(choice + rc)
  
  return res

def get_choices(s):
  if s[0] == "{":
    end = s.index("}")
    choices = s[1:end]
    remainder = s[end+1:]
    return (choices, remainder)
  else:
    return (s[0], s[1:])
  
# (abc)(abc)(abc)(abc) 
# where n is number of groups
# and m is max number of group members
  
# T: O(m**n)
# S: O(m**n)