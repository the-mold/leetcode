# Djikstra's algorithm
# solution explained https://www.youtube.com/watch?v=amvrKlMLuGY

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid)

        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0)) # (max_time, r, c)
        visited = set()
        visited.add((0, 0)) #first item is already in heap

        directions = [
            [-1,0],  #up
            [1, 0], #bottom
            [0, 1], #right
            [0,-1] #left
        ]

        while heap:
            t, r, c = heapq.heappop(heap)

            # check if we reached last cell
            if r == rows -1 and c == cols - 1:
                return t

            for dr, dc in directions:
                neighbor_r = r + dr
                neighbor_c = c + dc

                # skip cells that are out of bound and which were visited
                if neighbor_r < 0 or neighbor_r >= rows or neighbor_c < 0 or neighbor_c >= cols or (neighbor_r, neighbor_c) in visited:
                    continue

                # add the cell to min  with the maximum time seen on the path
                heapq.heappush(heap, (max(t, grid[neighbor_r][neighbor_c]), neighbor_r, neighbor_c))
                visited.add((neighbor_r, neighbor_c))

        # no need for it as valid answer is guaranteed by the problem
        return -1
      
#   Let N be the number of rows (and columns), so the grid has N x N cells.

# Time Complexity: O(N² log N)
# This complexity comes from the operations involving the min-heap (priority queue).

# Number of Vertices and Edges:
# The "vertices" in our graph are the cells of the grid. There are V = N * N = N² vertices.
# The "edges" are the connections between adjacent cells. Each cell has at most 4 neighbors, so the number of edges E is proportional to N².
# Heap Operations:
# Dijkstra's algorithm, when implemented with a min-heap, has a time complexity of O(E log V).
# In the worst case, we might push every cell onto the heap once. A heapq.heappush operation takes O(log(heap_size)) time. The heap can grow up to a size of N².
# Similarly, we will pop every cell from the heap once. A heapq.heappop also takes O(log(heap_size)) time.
# Putting It Together:
# We perform approximately N² push and N² pop operations.
# The cost of each operation is log(N²), which simplifies to 2 * log(N). In Big O notation, we drop the constant 2, so it's O(log N).
# Therefore, the total time complexity is N² (for each cell) times log N (for the heap operations), resulting in O(N² log N).
# Space Complexity: O(N²)
# The space complexity is determined by the data structures used to store information about the grid cells.

# heap (Min-Heap):
# In the worst-case scenario, the heap could contain an entry for every cell in the grid. This requires O(N²) space.
# visited Set:
# The visited set also stores a unique entry for each cell that has been visited. In the worst case, we visit every cell, so this also requires O(N²) space.
# Since both of these structures can grow to the size of the grid, the total extra space required is O(N²).