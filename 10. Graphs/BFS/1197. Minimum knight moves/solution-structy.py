import collections
def knight_attack(n, kr, kc, pr, pc):
  q = collections.deque()
  q.append((kr, kc, 0))
  visited = set()
  visited.add((kr,kc))

  while q:
    r, c, level = q.popleft()

    if r == pr and c == pc:
      return level

    # print("-----", get_options(r, c))
    for next_r, next_c in get_options(r, c):
      if not is_inbound(next_r, next_c, n):
        continue
        
      if (next_r, next_c) in visited:
        continue
      visited.add((next_r, next_c))

      q.append((next_r, next_c, level+1))

  return None

def get_options(r, c):
  opt = [
    # top
    (-2,-1),(-2,1),
    # right
    (-1,2),(1,2),
    # bottom
    (2,-1),(2,1),
    # left
    (-1,-2),(1,-2)
  ]

  res = []
  for dr, dc in opt:
    new_r = r + dr
    new_c = c + dc

    res.append((new_r, new_c))
    
  return res

def is_inbound(r, c, n):
  r_inbound = 0 <= r < n
  c_inbound = 0 <= c < n
  return r_inbound and c_inbound

# n is number of rows and number of cols

# T:O(n**n)
# S:O(n**n)