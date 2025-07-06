def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
  s1 = set(nums1)
  s2 = set(nums2)

  res1 = []
  for num in s1:
      if num not in s2:
          res1.append(num)
  
  res2 = []
  for num in s2:
      if num not in s1:
          res2.append(num)
  
  return [res1, res2]

#T:O(n+m)
#S:O(n+m)