def maxOperations(self, nums: list[int], k: int) -> int:
  res = 0
  seen = {}
  for idx, num in enumerate(nums):
      complement = k - num

      if complement in seen:
          res += 1
          if seen[complement] == 1:
              del seen[complement]
          else: 
              seen[complement] -= 1
      else:
          if num in seen:
              seen[num] += 1
          else:
              seen[num] = 1
  
  return res


#T:O(n)
#S:O(n)