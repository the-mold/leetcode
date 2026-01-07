def lowest_toll(highway_tolls, start_city, end_city):
  adj_map = {}
  for start, end, price in highway_tolls:
    if start not in adj_map:
      adj_map[start] = {}
    if end not in adj_map:
      adj_map[end] = {}

    adj_map[start][end] = price
    adj_map[end][start] = price
  
  return _lowest_toll(adj_map, start_city, end_city, set())

def _lowest_toll(adj_map, curr_city, end_city, visited):
  if curr_city == end_city:
    return 0

  if curr_city in visited:
    return float("inf")
  visited.add(curr_city)

  min_toll = float("inf")
  
  for neighbor in adj_map[curr_city]:
    cost = adj_map[curr_city][neighbor]
    min_toll = min(min_toll, cost + _lowest_toll(adj_map, neighbor, end_city, visited))

  visited.remove(curr_city)
  return min_toll

# T:O(n!)
# S:O(n**2) because of space needed for adj_map