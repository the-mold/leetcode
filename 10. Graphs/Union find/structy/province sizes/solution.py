def find(roots, node_idx):
  if roots[node_idx] == node_idx:
    return node_idx

  found = find(roots, roots[node_idx])
  roots[node_idx] = found
  return found

def union(roots, sizes, a, b):
  root_a = find(roots, a)
  root_b = find(roots, b)

  if root_a == root_b:
    return 

  if sizes[root_a] >= sizes[root_b]:
    roots[root_b] = root_a
    sizes[root_a] += sizes[root_b]
  else:
    roots[root_a] = root_b
    sizes[root_b] += sizes[root_a]
    
def province_sizes(n, roads):
  roots = [i for i in range(0, n)]
  sizes = [1 for i in range(0, n)]

  for a, b in roads:
    union(roots, sizes, a, b)

  res = []
  for i in range(0, n):
    if roots[i] == i:
      res.append(sizes[i])

  return res

# T: O(n + e*α(n)), where α(n) is inverse Acherman function on n. It is nearly constant. It grows very slowly.
# S:O(n)