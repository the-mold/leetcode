class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        def can_reach_end(max_effort: int) -> bool:
            """Check if a path exists with effort <= max_effort using BFS."""
            q = collections.deque([(0, 0)])
            visited = set([(0, 0)])
            
            while q:
                r, c = q.popleft()

                if r == rows - 1 and c == cols - 1:
                    return True

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                        # Check if the move is valid under the current max_effort
                        effort = abs(heights[nr][nc] - heights[r][c])
                        if effort <= max_effort:
                            visited.add((nr, nc))
                            q.append((nr, nc))
            return False

        # Binary search for the minimum possible effort
        left, right = 0, 10**6
        min_effort = right

        while left <= right:
            mid = (left + right) // 2
            if can_reach_end(mid):
                # This effort is possible, try for a smaller one
                min_effort = mid
                right = mid - 1
            else:
                # This effort is not enough, need to allow more
                left = mid + 1
                
        return min_effort
