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
    # if they are pointing to each other, then edge is redundunt
    return False

  if sizes[root_a] >= sizes[root_b]:
    roots[root_b] = root_a
    sizes[root_a] += sizes[root_b]
  else:
    roots[root_a] = root_b
    sizes[root_b] += sizes[root_a]

  return True

def extra_cable(num_computers, cables):
  roots = [i for i in range(num_computers)]
  sizes = [1 for i in range(num_computers)]

  for a, b in cables:
    could_union = union(roots, sizes, a, b)
    if not could_union:
      return (a, b)
  
# T: O(n + e*α(n)), where α(n) is inverse Ackerman function on n. It is nearly constant. It grows very slowly.
# S:O(n)
