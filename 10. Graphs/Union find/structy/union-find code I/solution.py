def find(root, node_idx):
  if root[node_idx] == node_idx:
    return node_idx
  return find(root, root[node_idx])

def union(root, node_a, node_b):
  node_a_root = find(root, node_a)
  node_b_root = find(root, node_b)

  if node_a_root == node_b_root:
    return

  root[node_b_root] = node_a_root

def count_components(n, edges):
  root = [i for i in range(0, n)]

  for node_a, node_b in edges:
    union(root, node_a, node_b)

  count = 0
  for i in range(0, n):
    if root[i] == i:
      count += 1

  return count


# T: O(N + E * N). Since in a connected graph E can be on the order of N^2, this can be very slow.