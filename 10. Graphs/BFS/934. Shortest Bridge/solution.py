class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # 1. find first island
        rows = len(grid)
        cols = len(grid[0])

        main_island = None
        for r in range(rows):
            for c in range(cols):
                candidate = find_fist_island(grid, r, c, set())
                if len(candidate) > 0:
                    main_island = candidate
                    break
            if main_island:
                break

        # 2. fill q with all cells of the first island
        q = collections.deque()
        for start, end in main_island:
            q.append((start, end, 0))

        visited = set(main_island)
        deltas = [(1,0),(0,-1),(-1,0),(0,1)]
        
        # 3. start BFS from each island cell to find the shortest distance to the other island
        while q:
            r, c, level = q.popleft()
            if grid[r][c] == 1 and (r,c) not in main_island:
                return level - 1

            for delta_r, delta_c in deltas:
                neighbor_r = r + delta_r
                neighbor_c = c + delta_c

                if not is_inbounds(grid, neighbor_r, neighbor_c):
                    continue
                
                if (neighbor_r, neighbor_c) not in visited:
                    visited.add((neighbor_r, neighbor_c))
                    q.append((neighbor_r, neighbor_c, level+1))
        return -1

def is_inbounds(grid, r, c):
    r_inbounds = 0 <= r < len(grid)
    c_inbounds = 0 <= c < len(grid[0])
    return r_inbounds and c_inbounds

def find_fist_island(grid, r, c, visited):
    if not is_inbounds(grid, r, c):
        return visited
    if grid[r][c] == 0:
        return visited

    if (r,c) in visited:
        return visited
    visited.add((r,c))  

    find_fist_island(grid, r + 1, c, visited)
    find_fist_island(grid, r - 1, c, visited)
    find_fist_island(grid, r, c + 1, visited)
    find_fist_island(grid, r, c - 1, visited)

    return visited