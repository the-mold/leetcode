def find_min_length(arr, k):
  freq_map = {}
  
  min_subarr_length = float("inf")
  l = 0
  r = 0
  while r < len(arr):
    freq_map[arr[r]] = freq_map.get(arr[r], 0) + 1

    while len(freq_map) > k:
      freq_map[arr[l]] -= 1
      if freq_map[arr[l]]== 0:
        del freq_map[arr[l]]
      l += 1

    if len(freq_map) == k:
      min_subarr_length = min(min_subarr_length, r - l + 1)
    
    r += 1
  
  return min_subarr_length if min_subarr_length != float("inf") else -1
