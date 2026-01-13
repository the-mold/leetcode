def paintHouse(costs):
  return _paintHouse(costs, 0, None, {})
                     
def _paintHouse(costs, curr_idx, prev_idx, memo):
  key = (curr_idx, prev_idx)
  if key in memo:
    return memo[key]
  
  if curr_idx == len(costs):
    return 0
  
  min_cost = float("inf")
  for i in range(len(costs[curr_idx])):
    if i != prev_idx:
      min_cost = min(
        min_cost,
        costs[curr_idx][i] + _paintHouse(costs, curr_idx + 1, i, memo)
      )
    
  memo[key] = min_cost
  return min_cost

# T:O(nm)
# S:O(nm)
