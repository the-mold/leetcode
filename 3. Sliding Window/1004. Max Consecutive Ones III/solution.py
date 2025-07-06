#Intuition: move the window by keeping max two zeros in it.

def longestOnes(self, nums: list[int], k: int) -> int:
  l = 0
  max_sequence_length = 0
  number_of_zeros_in_window = 0

  for r in range(len(nums)):
    if nums[r] == 0:
      number_of_zeros_in_window += 1
    
    while number_of_zeros_in_window > k:
      if nums[l] == 0:
        number_of_zeros_in_window -= 1
      l -= 1
    
    max_sequence_length = max(max_sequence_length, r - l + 1)
  
  return max_sequence_length

#T:O(n)
#S:O(1)
