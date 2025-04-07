def search(nums, target):
  left, right = 0, len(nums) - 1

  while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      left = mid + 1
    else: 
      right = mid - 1
  
  return -1

#T: O(log n)
#S: O(1)




search([1,2,3,4,5,6,7], 5)