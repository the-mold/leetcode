def merge_intervals(s):
  s.sort()

  merged = [s[0]]
  for curr_start, curr_end in s[1:]:
    prev_start, prev_end = merged[-1]

    if curr_start < prev_end:
      merged[-1] = [prev_start, max(prev_end, curr_end)]
    else:
      merged.append([curr_start, curr_end])  

  return merged


merge_intervals([[5,6], [1,3], [2,4]])
  