def pivotIndex(nums: List[int]) -> int:
  total = sum(nums)
  left_sum = 0

  for i in range(len(nums)):
      right_sum = total - left_sum - nums[i]
      if left_sum == right_sum:
          return i
          
      left_sum += nums[i]
  
  return -1

# T:O(n)
# S:O(1)
