def maxOperations(self, nums: List[int], k: int) -> int:
  # NEED TO SORT ARRAY FIRST
  nums.sort()
  
  res = 0
  l = 0
  r = len(nums) - 1

  while l < r:
    sum = nums[l] + nums[r]
    if sum == k:
      res += 1
      l += 1
      r -= 1
    elif sum > k:
      r -= 1
    else: 
      l += 1
  
  return res

# O(n log n)
# S(1)