def remove_duplicates(nums):
  k=1 #the first elem(index 0) is always unique

  for i in range(1, len(nums)):
    if nums[i] != nums[i-1]:
      nums[k] = nums[i]
      k += 1
  
  print("number of unique elems", k)

  return nums[:k]

#T: O(n)
#S: O(1)

print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))
