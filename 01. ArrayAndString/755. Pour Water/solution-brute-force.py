class Solution:
  def solve(self, terrain, v, k):
    res = terrain.copy()
    for _ in range(v):
      # check left
      if v > 0 and res[v] > res[v-1]:
        min_val = float("inf")
        min_idx = float("inf")
        for i in range(v-1, -1, -1):
          if min_val > res[i]:
            min_val = res[i]
            min_idx = i
        res[min_idx] += 1
        continue
      
      # check right
      if v != len(res) - 1 and res[v] > res[v+1]:
        min_val = float("inf")
        min_idx = float("inf")
        for i in range(v+1, len(res)):
          if min_val > res[i]:
            min_val = res[i]
            min_idx = i
        res[min_idx] += 1
        continue
      
      # add self
      res[k] += 1
    
    return res


Solution().solve([3,1,2], 2, 1)

# T:O(V*n)
# S:O(n)