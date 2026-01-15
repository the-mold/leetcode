import collections
def best_house_build(grid):
  q = collections.deque()
  visited = collections.defaultdict(set)
  total_distance = collections.defaultdict(int)

  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == 1:
        q.append(((r,c,0),(r,c))) # pos, src
        visited[(r,c)].add((r,c))

  num_houses = len(q)
  deltas = [
    (-1,0),
    (0,1),
    (1,0),
    (0,-1)
  ]
  
  while q:
    pos, src = q.popleft()
    r, c, dist = pos
    
    for dr, dc in deltas:
      new_r = r + dr
      new_c = c+ dc
      new_r_inbounds = 0 <= new_r < len(grid)
      new_c_inbounds = 0 <= new_c < len(grid[0])
      if not new_r_inbounds or not new_c_inbounds:
        continue

      new_pos = (new_r, new_c)
      if grid[new_r][new_c] != 0 or src in visited[new_pos]:
        continue
      visited[new_pos].add(src)

      new_dist = dist + 1
      q.append(((new_r, new_c, new_dist), src))
      total_distance[new_pos] += new_dist

  min_dist = float("inf")
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if total_distance[(r,c)] > 0 and len(visited[(r,c)]) == num_houses:
        min_dist = min(min_dist, total_distance[(r,c)])

  return -1 if min_dist == float("inf") else min_dist

# T:O(rc * rc)
# S:O(rc * rc)