from typing import List
import heapq

opt = [
  (-1,0),
  (0,1),
  (1,0),
  (0,-1)
]

class Solution:
  def solve(self, a: List[List[int]]) -> int:
    rows = len(a)
    cols = len(a[0])
    
    visited = set()
    visited.add((0,0))
    
    heap = []
    if rows > 0:
      heapq.heappush(heap, (-a[1][0], a[1][0], 1, 0))
      visited.add((1,0))
    if cols > 0:
      heapq.heappush(heap, (-a[0][1], a[0][1], 0, 1))
      visited.add((0,1))
      
    min_val = float("inf")
    while heap:
      _, val, r, c = heapq.heappop(heap)
      min_val = min(min_val, val)
      
      if r == rows - 1 and c == cols - 1:
        return min_val
      
      for dr, dc in opt:
        new_r = r + dr
        new_c = c + dc
        r_inbounds = 0 <= new_r < rows
        c_inbounds = 0 <= new_c < cols
        
        if not r_inbounds or not c_inbounds:
          continue
        
        if (new_r, new_c) in visited:
          continue
        visited.add((new_r, new_c))
        
        heapq.heappush(heap, (-a[new_r][new_c], a[new_r][new_c], new_r, new_c))
      
    return min_val
    

Solution().solve([[5,4,5],[1,2,6],[7,4,6]])