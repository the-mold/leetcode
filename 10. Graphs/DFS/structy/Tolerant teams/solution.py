import collections
def tolerant_teams(rivalries):
  adj_map = collections.defaultdict(list)
  for r1, r2 in rivalries:
    adj_map[r1].append(r2)
    adj_map[r2].append(r1)

  teams = {}

  for node in adj_map:
    if node in teams:
      continue
    
    if _can_create_team(adj_map, node, teams, True) == False:
      return False

  return True

def _can_create_team(adj_map, node, teams, curr_color):
  if node in teams:
    return teams[node] == curr_color

  teams[node] = curr_color
  for neighbor in adj_map[node]:
    if _can_create_team(adj_map, neighbor, teams, not curr_color) == False:
      return False

  return True

# e - number of edges
# n - number of nodes

#T:O(e)
#S:O(e)