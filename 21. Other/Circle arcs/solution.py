
def solve(arr):
  
  # Step 1. Transform intervals to normal values.
  #[[-90, 90]] => [360-90, 360], [0,90]
  sanitized = []
  for start, end in arr:
    # case [[-90, 90]]
    if start < 0 and end > 0:
      sanitized.append([360-abs(start), 360])
      sanitized.append([0, end])
    
    # case [[-90, -45]] 
    elif start < 0 and end < 0:
      sanitized.append([360-abs(start), 360 - abs(end)])
      
    # case with positive numbers
    else:
      sanitized.append([start, end])
  
  # Step 2. Sort and merge
  sanitized.sort(key=lambda x: x[0])
  
  merged = [sanitized[0]]
  for start, end in sanitized[1:]:
    prev_start = sanitized[-1][0]
    prev_end = sanitized[-1][1]
    
    if start <= prev_end:
      merged[-1] = [prev_start, max(end, prev_end)]
    else:
      merged.append([start, end])
      
  # Step 3. Calculate the percentage of the area covered
  total = 0
  for start, end in merged:
    total += end - start

  return total // 360 * 100

# T:O(n)
# S:O(n)
