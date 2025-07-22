class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        connections_tuple_dict = { (a,b) for a, b in connections }

        # build adjacency dict
        adj = {}
        for start, end in connections:
            adj.setdefault(start, []).append(end)
            adj.setdefault(end, []).append(start)

        visited = [False] * n
        self.reroute = 0

        def dfs(node_idx):
            for neighbour_idx in adj[node_idx]:
                if not visited[neighbour_idx]:  #O(1)
                    if (neighbour_idx, node_idx) not in connections_tuple_dict:
                        self.reroute += 1
                    visited[neighbour_idx] = True
                    dfs(neighbour_idx)


        visited[0] = True
        dfs(0)
                
        return self.reroute


# Intuition:
# `connections_tuple_dict` captures the current state of routes and the line `if (neighbour_idx, node_idx) not in connections_tuple_dict` checks what the route should be.
# If it is not present in `connections_tuple_dict` then the route must be rerouted.

# T:O(n)
# S:O(n)

# Time Complexity: O(N)
# The overall time complexity is linear with respect to the number of cities. Here's the breakdown:

# Building connections_tuple_dict: You iterate through all N - 1 connections once to build the set. This takes O(N) time.
# Building the Adjacency List adj: You iterate through the N - 1 connections again to build the undirected graph. This also takes O(N) time.
# DFS Traversal:
# The dfs function visits every node and every edge exactly once, thanks to the visited array.
# For each node, it iterates through its neighbors. Over the entire traversal, each edge is considered twice (once from each direction).
# Inside the loop, the check (neighbour_idx, node_idx) not in connections_tuple_dict is a hash set lookup, which takes O(1) time on average.
# Therefore, the total time spent in the DFS is proportional to the number of nodes plus the number of edges, which is O(N + (N-1)), simplifying to O(N).
# Since all steps are linear, the total time complexity is O(N).

# Space Complexity: O(N)
# The space complexity is also linear, determined by the data structures used to store the graph and manage the traversal.

# connections_tuple_dict: This set stores all N - 1 original connections. This requires O(N) space.
# Adjacency List adj: The dictionary stores an entry for each of the N nodes and lists all 2 * (N - 1) directed edges of the undirected graph. This requires O(N) space.
# visited Array: This is a boolean array of size N, requiring O(N) space.
# Recursion Stack: In the worst-case scenario (a graph that is a long, unbranched chain), the recursion depth of the dfs could be up to N. This means the call stack could also grow to a size of O(N).
# Because all space requirements scale linearly with the number of cities, the overall space complexity is O(N).