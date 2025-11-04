# Djikstra's algorithm

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        heap = []
        heapq.heappush(heap, (0, 0, 0)) #push first cell (effort, r, c)
        visited = set()
        visited.add((0,0))

        directions = [
            (-1,0), #up
            (1,0), #down
            (0,-1), #left
            (0,1)
        ]

        while heap:
            curr_max_val, r, c = heapq.heappop(heap)
            visited.add((r, c))

            # we reached the end
            if r == rows - 1 and c == cols - 1:
                return curr_max_val

            for rd, cd in directions:
                nr = rd + r #neighbor rows
                nc = cd + c #neighbor columns

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr,nc) in visited:
                    continue
                
                newDiff = max(curr_max_val, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(heap, (newDiff, nr, nc))

        return -1

# Time Complexity: O(R * C * log(R * C))
# The time complexity is determined by the operations on the min-heap within the main loop.

# Heap Size: In the worst case, the heap can store an entry for every cell in the grid. Therefore, the maximum size of the heap is N = R * C.
# Heap Operations:
# heappush: Each cell is pushed onto the heap. A push operation costs O(log N).
# heappop: Each cell is eventually popped from the heap to be processed. A pop operation also costs O(log N).
# Main Loop: The while loop runs as long as the heap is not empty. Since each cell is processed (popped) at most once due to the visited set logic, the loop will execute approximately N times.
# Total Time: We perform N heappop operations and up to 4 * N (for all neighbors) heappush operations. The dominant cost is N operations, each taking O(log N).
# Therefore, the total time complexity is O(N * log N), which translates to O(R * C * log(R * C)).

# Space Complexity: O(R * C)
# The space complexity is determined by the storage required for the auxiliary data structures.

# heap: As mentioned, the heap can store up to N = R * C elements in the worst case. This requires O(R * C) space.
# visited Set: The visited set stores the coordinates of each cell that has been processed. In the worst case, it will also store all N cells. This requires O(R * C) space.
# Since both data structures scale linearly with the number of cells, the total space complexity is O(R * C).