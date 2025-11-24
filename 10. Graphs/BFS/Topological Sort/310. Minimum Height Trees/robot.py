from collections import defaultdict, deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # --- Edge Case: A single node tree ---
        if n == 1:
            return [0]
        
        # --- Step 1: Build the Graph and Initial Degrees ---
        
        # 'adj' will be our adjacency list for the undirected graph.
        adj = defaultdict(list)
        # 'degrees' will store the number of edges connected to each node.
        degrees = [0] * n
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degrees[u] += 1
            degrees[v] += 1
            
        # --- Step 2: Find the Initial Leaves ---
        
        # A leaf node in a tree has a degree of 1.
        # We start our "peeling" process from these leaves.
        leaves = deque()
        for i in range(n):
            if degrees[i] == 1:
                leaves.append(i)
                
        # --- Step 3: Peel Away Layers Until We Reach the Center ---
        
        remaining_nodes = n
        
        # We continue until 2 or fewer nodes remain. These will be the MHT roots.
        # A tree can have 1 MHT root (e.g., a star graph) or 2 (e.g., a path graph).
        while remaining_nodes > 2:
            # Get the number of leaves in the current layer.
            num_leaves = len(leaves)
            remaining_nodes -= num_leaves
            
            # Process and "remove" all leaves in the current layer.
            for _ in range(num_leaves):
                leaf = leaves.popleft()
                
                # For each neighbor of the removed leaf...
                for neighbor in adj[leaf]:
                    # ...decrement its degree because we've removed the edge to the leaf.
                    degrees[neighbor] -= 1
                    
                    # If the neighbor has now become a leaf, add it to the queue
                    # for the next layer of peeling.
                    if degrees[neighbor] == 1:
                        leaves.append(neighbor)
                        
        # --- Step 4: The Remaining Nodes are the MHT Roots ---
        
        # The nodes left in the 'leaves' queue are the centermost nodes.
        return list(leaves)

# Example 1
# n = 4, edges = [[1,0],[1,2],[1,3]]
# print(Solution().findMinHeightTrees(n, edges))  # Output: [1]

# Example 2
# n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# print(Solution().findMinHeightTrees(n, edges))  # Output: [3, 4]