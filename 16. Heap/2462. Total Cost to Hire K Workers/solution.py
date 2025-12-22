class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        left = []
        right = []
        l, r = 0, len(costs) - 1
        total = 0

        # preload first candidates into heaps
        for _ in range(candidates):
            if l <= r:
                heapq.heappush(left, (costs[l], l))
                l += 1 

        for _ in range(candidates):
            if l <= r:
                heapq.heappush(right, (costs[r], r))
                r -= 1 

        # start k selection sessions
        for _ in range(k):
            if left and right:
                if left[0] <= right[0]:
                    cost, _ = heapq.heappop(left)
                    total += cost
                    if l <= r:
                        heapq.heappush(left, (costs[l], l))
                        l += 1
                else:
                    cost, _ = heapq.heappop(right)
                    total += cost
                    if l <= r:
                        heapq.heappush(right, (costs[r], r))
                        r -= 1
            elif left:
                cost, _ = heapq.heappop(left)
                total += cost
                if l <= r:
                    heapq.heappush(left, (costs[l], l))
                    l += 1
            elif right:
                cost, _ = heapq.heappop(right)
                total += cost
                if l <= r:
                    heapq.heappush(right, (costs[r], r))
                    r -= 1
        
        return total
      
# Time: O((k + candidates) log candidates)
# Space: O(candidates)
