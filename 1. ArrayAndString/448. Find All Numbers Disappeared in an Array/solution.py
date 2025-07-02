def findAllMissingNumbers(nums):
  sett = set(nums)    #T:O(n)    <- this takes time to insert every element from nums into set
  ans = []
  n = len(nums)

  for i in range(1, n + 1):  #T:O(n)
    if i not in sett:
      ans.append(i)
  
  return ans

#T:O(n)
#S:O(n)
