def kthelement(numbers, k):
  numbers.sort()
  return numbers[-k]

#T:O(n log n)
#S:O(n)