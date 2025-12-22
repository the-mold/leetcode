import heapq
def k_smallest(nums, k):
  max_heap = []
  for num in nums: # n
    item = (-num, num) 
    heapq.heappush(max_heap, item) #log k
    if len(max_heap) > k:
      heapq.heappop(max_heap)

  res = []
  while len(max_heap) > 0:
    item = heapq.heappop(max_heap)
    res.append(item[1])
    
  return res[::-1]

# T:O(n logk)
# S:O(k)
