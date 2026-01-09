def knightly_number(n, m, kr, kc, pr, pc):
  return _knightly_number(n, m, kr, kc, pr, pc, {})

options = [
  (-2,-1),
  (-2,1),
  (-1,2),
  (1,2),
  (2,1),
  (2,-1),
  (-1,-2),
  (1,-2)
]

def _knightly_number(n, m, r, c, pr, pc, memo):
  key = (r, c, m)
  if key in memo:
    return memo[key]
    
  if m == 0 and r == pr and c == pc:
    return 1

  if m <= 0:
    return 0
  
  total = 0
  for dr, dc in options:
    next_r = r + dr
    next_c = c + dc
    r_inbounds = 0 <= next_r < n
    c_inbounds = 0 <= next_c < n
    if not r_inbounds or not c_inbounds:
      continue
    
    total += _knightly_number(n, m - 1, r + dr, c + dc, pr, pc, memo)

  memo[key] = total
  return total

# T:O(m*n*n), for three args that change
# S:O(m*n*n)