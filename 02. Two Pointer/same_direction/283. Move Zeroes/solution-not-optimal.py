def moveZeroes(self, nums: List[int]) -> None:
  """
  Do not return anything, modify nums in-place instead.
  """
  l = len(nums)
  l_zero = 0
  res = []

  for num in nums:
      # count number of zeros and 
      if num == 0:
          l_zero += 1
      else:
          #make array of non-zeros in order that they appear in array
          res.append(num)
  
  res += [0] * l_zero

  # reassign numbers to the original array(required by the problem)
  for idx, num in enumerate(nums):
      nums[idx] = res[idx]

#T: O(n)
#S: O(n)
