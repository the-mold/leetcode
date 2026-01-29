class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.defaultdict(int)
        for num in nums: # O(n)
            d[num] += 1

        heap = []
        for key in d: # O(n)
          heap.append((-d[key], key)) # O(1)
          
        heapq.heapify(heap) # O(n)

        res = []
        for _ in range(k): #O(k)
            _, key = heapq.heappop(heap) #O(logn)
            res.append(key)
        
        return res
      
# T:O(n + k*logn) 
# S:O(n)