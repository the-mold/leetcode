def find(root, node_idx):
  if root[node_idx] == node_idx:
    return node_idx

  found = find(root, root[node_idx])
  # Path compression optimization:
  # make eacg node to point to its root. It this way consequent root lookups will be O(1)
  root[node_idx] = found
  
  return found

def union(root, sizes, node_a, node_b):
  root_a = find(root, node_a)
  root_b = find(root, node_b)

  if root_a == root_b:
    return

  # Union by size optimization:
  # in naive implementation there is a risk of building a linked list with O(n) root lookup.
  # "Union by size optimization" builds a "bushy" tree where nodes have immediate or fast connection to the root.
  #It keeps the trees shallow and bushy. It guarantees that the depth of any tree is at most O(log N).
  if sizes[root_a] >= sizes[root_b]:
    root[root_b] = root_a
    sizes[root_a] += sizes[root_b]
  else:
    root[root_a] = root_b
    sizes[root_b] += sizes[root_a]

def count_components(n, edges):
  root = [i for i in range(0, n)]
  sizes = [1 for i in range(0, n)]

  for node_a, node_b in edges:
    union(root, sizes, node_a, node_b)

  count = 0
  for i in range(0, n):
    if root[i] == i:
      count += 1

  return count

# T: O(n + e*α(n)), where α(n) is inverse Acherman function on n. It is nearly constant. It grows very slowly.

# S: O(n)