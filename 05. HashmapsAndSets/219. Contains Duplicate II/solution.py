def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
  last_seen = {}

  for idx, num in enumerate(nums):
      if num in last_seen and idx - last_seen[num] <= k:
          return True
      last_seen[num] = idx

  return False

#T:O(n)
#S:O(n)
