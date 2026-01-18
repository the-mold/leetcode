def solve(workers, bikes):
  W = len(workers)
  B = len(workers)
  
  distances = collections.defaultdict(list)
  # calculate Manhatten distance from each worker to each bike
  # Manhattan distance is |x_{1}-x_{2}|+|y_{1}-y_{2}|
  for w in range(W):
    for b in range(B):
      dist = abs(workers[w][0] - bikes[b][0]) + abs(workers[w][1] - bikes[b][1])
      distances[dist].append((w, b))
      
  workers_used = set()
  bikes_used = set()
  
  res = [None] * W
  
  for key in sorted(distances.keys()):
    for w, b in distances[key]:
      if w not in workers_used and b not in bikes_used:
        workers_used.add(w)
        bikes_used.add(b)
        
        res[w] = b 
  
  return res

# w - workers
# b - bikes
# R - distances

# T:O(w*b + R log R)
# S:O(w*b)
