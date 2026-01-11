def knapsack(values, weights, weight_limit):
  return _knapsack(values, weights, weight_limit, 0, {})

def _knapsack(values, weights, weight_limit, idx, memo):
  key = (weight_limit, idx)
  if key in memo:
    return memo[key]

  if weight_limit < 0:
    return float("-inf")
  if idx == len(weights):
    return 0

  take = values[idx] + _knapsack(values, weights, weight_limit - weights[idx], idx + 1, memo)
  not_take = _knapsack(values, weights, weight_limit, idx + 1, memo)
  memo[key] = max(take, not_take)

  return memo[key]

# n = number of items
# m = weight limit

#T:O(n*m)
#S:O(n*m)