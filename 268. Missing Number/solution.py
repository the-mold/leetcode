# Bad solution

def missingNumber(nums) -> int:
  nums.sort()
  for i in range(len(nums)):
    if nums[i+1] - nums[i] > 1:
      return nums[i] + 1
    
missingNumber([0,1,3,5,4])


Time:   O(n log n)   ## this is always the worst case complexity when you have sorting in python
Memory: O(1)



# A bit better solution: avoid sorting
def missingNumber(nums) -> int:
  numss = set(nums)
  for i in range(len(nums) + 1):
    if i not in numss:
      return i

Time:   O(n)
Memory: O(n)



# The best solution
def missingNumber(nums) -> int:
  act_sum = sum(nums)
  n = len(nums)                     # for sequence starting at 1, you do `n = len(nums) + 1`
  exp_sum = n * (n + 1) / 2         # arithmeric sum for natural numbers that start in sequence

  return exp_sum - act_sum

Time:   O(n)
Memory: O(1)
