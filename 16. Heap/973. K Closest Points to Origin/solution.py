import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        dic = {}

        # Store both distance and point in heap
        for x, y in points: # n iterations
            euclidean_distance = ((x-0)**2 + (y-0)**2)**0.5
            # Note: heap compares tuples left to right when making heap order 
            heapq.heappush(min_heap, (euclidean_distance, [x, y]))  # O(log n)

        # Pop k smallest distances
        res = []
        for i in range(k):
            # Note! You to get the smallest elements, you need to pop items all the time.
            # min_heap[0] is always the smallest element
            # min_heap[1] is NOT the second smallest element! You need to pop the first element and then read min_heap[0] again to get the second smallest.
            euclidean_distance, point = heapq.heappop(min_heap)
            res.append(point)
        
        return res

# Time complexity: O(N⋅log N)

# Space complexity: O(N)
# - heap is space N
# - res is space k