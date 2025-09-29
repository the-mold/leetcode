def moveZeroes(self, nums: list[int]) -> None:
  lastNonZeroItem = 0

  for i in range(len(nums)):
    if nums[i] != 0:
      nums[lastNonZeroItem], nums[i] = nums[i], nums[lastNonZeroItem]
      lastNonZeroItem += 1

#T: O(n)
#S: O(1)