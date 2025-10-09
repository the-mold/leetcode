import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for st in stones:
            heapq.heappush(heap, -st)

        while heap and len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if y != x:
                y, x = -y, -x
                heapq.heappush(heap, -(y - x))


        if len(heap) == 0:
            return 0
        else:
            return -heap[0]

# T:O(n log n), heap operation is logn. The while loop is n.
# S:O(n)
