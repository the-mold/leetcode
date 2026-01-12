class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_count = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c,0))
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        opt = [
            (-1, 0),
            (0,1),
            (1,0),
            (0,-1)
        ]

        max_t = 0
        while q:
            r, c, t = q.popleft()
            max_t = max(max_t, t)

            for dr, dc in opt:
                next_r = dr + r
                next_c = dc + c
                next_r_inbounds = 0 <= next_r < rows
                next_c_inbounds = 0 <= next_c < cols
                if not next_r_inbounds or not next_c_inbounds:
                    continue
                
                if grid[next_r][next_c] == 1:
                    if (next_r, next_c) in visited:
                        continue
                    visited.add((next_r, next_c))
                    fresh_count -= 1
                    q.append((next_r, next_c, t + 1))
    
        if fresh_count > 0:
            return -1
        else:
            return max_t
          
# T:O(nm)
# S:O(nm)