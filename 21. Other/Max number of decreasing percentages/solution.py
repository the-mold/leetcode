

def solve(arr):
  stake = float("-inf")
  last_percentage = float("inf")
  for row in arr:
    # find first False
    last_true_idx = binary_search_last_true(row)
    perc = 0
    if last_true_idx != -1:
      perc = last_true_idx / (len(row) - 1)
      
    if perc < last_percentage:
      stake += 1
    else:
      stake = 1
    last_percentage = perc
  
  return stake
    
    
def binary_search_last_true(rows):
  l = 0
  r = len(rows) - 1
  res = -1
  while l <= r:
    mid = (l + r) // 2
    
    if rows[mid] == True:
      # found potential solution. Continue searching.
      res = mid
      l = mid + 1
    else:
      r = mid - 1
  
  return res
    
# n - number of entries in initial input
# m - length of a single record

# T: O(n * log m)
# S: O(1)