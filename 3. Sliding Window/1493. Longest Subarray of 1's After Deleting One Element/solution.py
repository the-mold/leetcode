#Intuition
# We have a binary array nums with size N; we need to delete exactly one element from it 
# and then return the longest subarray having only 1. Since we need to maximize the count 
# of 1 in the subarray, we should not delete a 1, except in the case when the array has 
# all elements as 1 (then we don't have a choice).

# Although we need a subarray with all elements as 1, we can afford to have one 0 as we can 
# delete it. We will keep a window and keep adding elements as long as the count of 0s in it 
# doesn't exceed one. Once the number of 0s exceeds one, we will shrink the window from the 
# left side till the count of 0 comes under the limit; then, we can compare the size of the 
# current window with the longest subarray we have got so far.

def longestSubarray(self, nums: list[int]) -> int:
  l = 0
  zero_count = 0
  max_sequence_length = 0

  for r in range(len(nums)):
      # move r to the right
      if nums[r] == 0:
          zero_count += 1

      # if needed, move left to the right
      while zero_count > 1:
          if nums[l] == 0:
              zero_count -= 1
          l += 1

      # find the largest sequence
      max_sequence_length = max(max_sequence_length, r - l + 1)


  if max_sequence_length == 0:
      return 0
  
  # return max sequence without the one deleted number
  return max_sequence_length - 1

#T:O(n) 
#S:O(n) 