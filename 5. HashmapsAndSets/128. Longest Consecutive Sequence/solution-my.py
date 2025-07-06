def longestConsecutive(self, nums: List[int]) -> int:
  if not nums:
      return 0

  snums = set(nums)

  nums_sorted = sorted(list(snums))
  max_sequence = 0
  current_sequence = 0
  for i, num in enumerate(nums_sorted):
      if i + 1 < len(nums_sorted) and nums_sorted[i+1] - num == 1:
          current_sequence += 1
      else:
          max_sequence = max(max_sequence, current_sequence)
          current_sequence = 0
  
  return max_sequence + 1       #add 1 to account for the very first element