
def solution(n: int, edges: list[list[int]]):
  visited = [False] * n

  def dfs(node_idx):
    visited[node_idx] = True

    for edge in edges:
      if node_idx in edge:
        for edge_key in edge:
          if edge_key != node_idx and not visited[edge_key]:
            dfs(edge_key)

  connected_components = 0
  for node_idx in range(n):
    if not visited[node_idx]:
      connected_components += 1
      dfs(node_idx)
  
  return connected_components


# Time Complexity: O(N * E)
# This is the major difference. The complexity is significantly worse due to how neighbors are found.

# Outer Loop:
# python
# for node_idx in range(n):
#   if not visited[node_idx]:
#     # ...
#     dfs(node_idx)
# This loop runs N times, and the if condition ensures that dfs is called once for each connected component.
# DFS Function (dfs):
# python
# def dfs(node_idx):
#   visited[node_idx] = True
#   for edge in edges:  # <--- The source of inefficiency
#     if node_idx in edge:
#       # ...
#       dfs(neighbor_key)
# The critical part is the for edge in edges: loop. This loop runs E times every single time dfs is called.
# The dfs function is called exactly once for every node in the graph over the course of the entire algorithm.
# This means for each of the N nodes, you are iterating through all E edges to find its neighbors.
# Total Calculation: The total work is the sum of the work done for each node. Since the work for each node involves an O(E) loop, the total time complexity is N * O(E) = O(N * E).
# To put this in perspective, if you have a graph with 1,000 nodes and 10,000 edges, this algorithm would perform roughly 10 million operations (1,000 * 10,000). The more efficient O(N + E) solution would perform closer to 11,000 operations (1,000 + 10,000), which is a massive difference.

# Space Complexity: O(N)
# The space complexity is determined by the auxiliary data structures and the recursion depth.

# Visited Array (visited):
# This is an array of size N.
# Space: O(N)
# Recursion Stack (for dfs):
# In the worst-case scenario of a "line graph" (e.g., edges [[0,1], [1,2], [2,3], ...]), the recursion can go N levels deep.
# Space: O(N)
# The total auxiliary space complexity is O(N) + O(N), which simplifies to O(N). (This does not include the space for the input edges list, which is O(E)).