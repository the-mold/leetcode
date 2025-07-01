def arrayHasDuplicates(arr):
  seen = {}
  for i, num in enumerate(arr):
    if num in seen:
      return True
    seen[num] = i
#T: O(n)
#S: O(n)


def arrayHasDuplicates(arr):
  return len(arr) > len(set(arr))

#T:O(1)
#S:O(n)
