
def solution(n: int, edges: list[list[int]]):
  # 1. Build an adjacency list for efficient neighbor lookup
  adj = {}
  for s, f in edges:
    adj.setdefault(s, []).append(f)
    adj.setdefault(f, []).append(s)

  print("adj", adj) # eg. {0: [1], 1: [0, 2], 2: [1], 3: [4], 4: [3]}

  visited = [False] * n
  graph_components = 0

  def dfs(node_idx):
    visited[node_idx] = True
    for neighbor_idx in adj[node_idx]:
      if not visited[neighbor_idx]:
        dfs(neighbor_idx)

  for node_idx in range(n):
    if not visited[node_idx]:
      graph_components += 1
      dfs(node_idx) 

  return graph_components


solution(5, [[0,1],[1,2],[3,4]])



# Time Complexity: O(N + E)
# The total time complexity is a sum of the main parts of the algorithm:

# Building the Adjacency List:
# python
# adj = {}
# for s, f in edges:
#   adj.setdefault(s, []).append(f)
#   adj.setdefault(f, []).append(s)
# This code iterates through every edge in the edges list exactly once.
# The operations inside the loop (setdefault and append) take, on average, constant time, O(1).
# Therefore, the time taken for this part is directly proportional to the number of edges, E.
# Complexity: O(E)
# DFS Traversal:
# python
# visited = [False] * n
# # ...
# def dfs(node_idx):
#   # ...
# for node_idx in range(n):
#   if not visited[node_idx]:
#     graph_components += 1
#     dfs(node_idx)
# The main for loop iterates through all N nodes. The if not visited[node_idx] check ensures that the dfs function is only called once for each connected component.
# The key is to analyze the total work done by all calls to dfs combined.
# During the entire execution, the dfs function visits each node (N) and each edge (E) exactly once. A node is marked visited and never explored again. Its list of neighbors (representing its edges) is iterated through once.
# Since each edge (u, v) is stored twice in the adjacency list (once for u and once for v), the traversal will look at 2 * E edge entries in total.
# Complexity: O(N + E)
# Combining these parts, the overall time complexity is O(E) + O(N + E), which simplifies to O(N + E). This is an efficient way to traverse a graph.

# Space Complexity: O(N + E)
# The space complexity is determined by the storage required for your data structures and the recursion stack.

# Adjacency List (adj):
# This dictionary stores a key for each node that has an edge. In the worst case, it stores N keys.
# The values are lists of neighbors. The total number of items across all these lists is 2 * E, since each edge is added twice.
# Space: O(N + E)
# Visited Array (visited):
# This is an array of size N to keep track of visited nodes.
# Space: O(N)
# Recursion Stack (for dfs):
# The dfs function calls itself recursively. The maximum depth of the recursion depends on the shape of the graph.
# In the worst-case scenario (e.g., a graph that is a single long chain of nodes), the recursion depth could be up to N.
# Space: O(N)
# The total space is O(N + E) + O(N) + O(N). The dominant term is the adjacency list, so the overall space complexity simplifies to O(N + E).
