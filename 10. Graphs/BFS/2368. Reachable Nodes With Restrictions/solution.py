class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adj_map = defaultdict(list)
        for start, end in edges:
            adj_map[start].append(end)
            adj_map[end].append(start)

        count = 0
        q = collections.deque()
        q.append(0)
        visited = set(restricted)

        while q:
            node = q.popleft()
            if node in visited:
                continue
            
            visited.add(node)
            count += 1

            for neighbor in adj_map[node]:
                q.append(neighbor)
        
        return count
    
# T:O(n)
# S:O(n)