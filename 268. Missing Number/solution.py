# Bad solution

def missingNumber(nums) -> int:
  nums.sort()
  for i in range(len(nums)):
    if nums[i+1] - nums[i] > 1:
      return nums[i] + 1
    
missingNumber([0,1,3,5,4])


Complexity: O(n log n)   ## this is always the worst case complexity when you have sorting in python



# A bit better solution: avoid sorting
def missingNumber(nums) -> int:
  numss = set(nums)
  for i in range(len(nums) + 1):
    if i not in numss:
      return i

Complexity: O(n)   ## this is always the worst case complexity when you have sorting in python



# The best solution
def missingNumber(nums) -> int:
  act_sum = sum(nums)
  n = len(nums)
  exp_sum = n * (n + 1) / 2

  return exp_sum - act_sum

Complexity: O(log n)   ## this is always the worst case complexity when you have sorting in python
