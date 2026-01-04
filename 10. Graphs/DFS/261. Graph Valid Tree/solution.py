import collections
def rare_routing(n, roads):
  adj_map = collections.defaultdict(list)
  for r1, r2 in roads:
    adj_map[r1].append(r2)
    adj_map[r2].append(r1)
  
  visited = set()
  
  if _rare_routing(adj_map, 0, visited, None) == False:
    return False

  return len(visited) == n

def _rare_routing(adj_map, node, visited, last_node):
  if node in visited:
    return False

  visited.add(node)

  for neighbor in adj_map[node]:
    if neighbor == last_node:
      continue
    if _rare_routing(adj_map, neighbor, visited, node) == False:
      return False

  return True