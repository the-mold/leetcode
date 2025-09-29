def min_distance(arr):
  if not arr:
    return -1
  
  min_distance = float("inf")
  
  dic = {}
  for idx, num in enumerate(arr):
    if num in dic:
      min_distance = min(min_distance, idx - dic[num])
    
    # always update idx because maybe next occurence of the number will be even shorter.
    dic[num] = idx
    
  return min_distance if min_distance != float("inf") else -1
    

min_distance([3,2,1,2,3])
