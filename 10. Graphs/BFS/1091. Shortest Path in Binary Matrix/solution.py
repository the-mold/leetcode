class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # check if either start or end are walls
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1

        deltas = [
            (0,1),
            (1,1),
            (1,0),
            (1,-1),
            (0,-1),
            (-1,-1),
            (-1,0),
            (-1,1)
        ]

        visited = set((0,0))
        q = collections.deque()
        q.append((0,0,1))

        while q:
            r, c, level = q.popleft()
            if r == rows - 1 and c == cols - 1:
                return level

            for delta_r, delta_c in deltas:
                neighbor_r = r + delta_r
                neighbor_c = c + delta_c

                r_inbound = 0 <= neighbor_r < rows
                c_inbound = 0 <= neighbor_c < cols

                if not r_inbound or not c_inbound:
                    continue
                
                # road blocked
                if grid[neighbor_r][neighbor_c] == 1:
                    continue

                if (neighbor_r,neighbor_c) in visited:
                    continue
                visited.add((neighbor_r,neighbor_c))

                q.append((neighbor_r, neighbor_c, level + 1))
        
        return -1
      
#T:O(nm)
#S:O(nm)