def searchInsert(nums, target):
  left, right = 0, len(nums) - 1

  while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  
  return left

#T: O(log n)   , because you are reducing every time array by 2.
#S: O(1)

print(searchInsert([1,3,5,6], 5))  # Output: 2
print(searchInsert([1,3,5,6], 2))  # Output: 1
print(searchInsert([1,3,5,6], 7))  # Output: 4
print(searchInsert([1,3,5,6], 0))  # Output: 0
