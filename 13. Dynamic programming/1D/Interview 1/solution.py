def ways(total, k) -> int:
  memo = {}
  
  MOD = (10**9+7)
  
  def helper(target, min_k):
    if target == 0:
      return 1
    if target < 0:
      return 0
    if min_k > k:
      return 0
    
    key = (target, min_k)
    if key in memo:
      return memo[key]

    # try to use bigger min_k 
    res = helper(target, min_k + 1)
    
    # use the current min_k if the target is smaller
    if target >= min_k:
      res = (res + helper(target - min_k, min_k))
      
    res = res % MOD
    memo[key] = res
    return res
  
  return helper(total, 1)
