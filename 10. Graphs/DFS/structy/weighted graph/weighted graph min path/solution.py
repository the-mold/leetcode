def weighted_graph_min_path(graph, src, dst):
  return _weighted_graph_min_path(graph, src, dst, set())

def _weighted_graph_min_path(graph, node, dst, visited):
  if node == dst:
    return 0

  if node in visited:
    return float("inf")
  visited.add(node)

  min_path = float("inf")
  for neighbor in graph[node]:
    weight = graph[node][neighbor]
    min_path = min(min_path, weight + _weighted_graph_min_path(graph, neighbor, dst, visited))

  visited.remove(node)
  return min_path
  
# T:O(n!)
# S:O(n)
