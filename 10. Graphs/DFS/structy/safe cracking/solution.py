def safe_cracking(hints):
  num_parents = {}
  for start, end in hints:
    num_parents[start] = 0
    num_parents[end] = 0
    
  adj_map = {}
  for start, end in hints:
    if start not in adj_map:
      adj_map[start] = []
    if end not in adj_map:
      adj_map[end] = []
    adj_map[start].append(end)
    num_parents[end] += 1

  q = [node for node in num_parents if num_parents[node] == 0]

  res = []
  visited = set(q)
  while q:
    node = q.pop()
    res.append(node)

    for neighbor in adj_map[node]:
      if neighbor in visited:
        continue

      num_parents[neighbor] -= 1
      if num_parents[neighbor] == 0:
        q.append(neighbor)
        visited.add(neighbor)

  return "".join([str(item) for item in res])

# n - nodes
# e - edges

# T:O(n+e)
# S:O(n)