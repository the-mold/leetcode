def canJump(nums: list[int]):
  last_idx = len(nums) - 1
  goal = last_idx

  # go from finish to the start and move the goal pointer to the left every time, you can reach it.
  # Move it to the left every time.
  for i in range(last_idx, -1, -1):
    if i + nums[i] >= goal:
      goal = i
  
  # we reached the start(0 index) it means, that we can reach the finish from start
  if goal == 0:
    return True
  
  return False

#T:O(n)
#S:O(1)