class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = [] # max heap! store return the largest diffs first

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue

            # use bricks by default
            bricks -= diff
            # append to max heap
            heapq.heappush(heap, -diff)

            if bricks < 0:
                if ladders == 0:
                    return i
                ladders -= 1
                
                bricks += -heapq.heappop(heap) # here you retreive the largest diff so far, "use" ladder for it and retrieve number of bricks
        
        # if you are here, you reached the end
        return len(heights) - 1

# T:O(n logn)
# S:O(n)