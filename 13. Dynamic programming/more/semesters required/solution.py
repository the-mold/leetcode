def semesters_required(num_courses, prereqs):
  adj_map = {}
  for i in range(num_courses):
    adj_map[i] = []
  for start, end in prereqs:
    adj_map[start].append(end)
  
  distances = {}
  for i in range(num_courses):
    if i in adj_map and len(adj_map[i]) == 0:
      distances[i] = 1

  for i in range(num_courses):
    _semesters_required(num_courses, adj_map, i, distances)

  return max(distances.values())

def _semesters_required(num_courses, adj_map, i, distances):
  if i in distances:
    return distances[i]

  max_distance = 0
  for neighbor in adj_map[i]:
    max_distance = max(max_distance, 1 + _semesters_required(num_courses, adj_map, neighbor, distances))

  distances[i] = max_distance
  return max_distance