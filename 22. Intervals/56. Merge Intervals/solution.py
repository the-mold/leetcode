def mergeIntervals(intervals):
  if not intervals:
      return []
  
  intervals.sort(key=lambda x: x[0])

  ans = [intervals[0]]

  for current_start, current_end in intervals[1:]:
      prev_start, prev_end = ans[-1]

      if prev_end >= current_start:
          ans[-1][1] = max(current_end, prev_end) 
      else:
          ans.append([current_start, current_end])

  return ans

#T: O(n log n)
#S: O(n)

mergeIntervals([[1,3],[2,6],[8,10],[15,18]])