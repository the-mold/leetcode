class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_map = collections.defaultdict(list)
        for start, end, time in times:
            adj_map[start].append((end, time))

        min_heap = [(0, k)] #cost of start node is 0
        visit = set()
        curr_max_time = 0

        while min_heap:
            node_time, node = heapq.heappop(min_heap)
            if node in visit:
                continue

            curr_max_time = max(curr_max_time, node_time)

            visit.add(node)                

            for neighbor, neighbor_time in adj_map[node]:
                if neighbor in visit:
                    continue
                
                heapq.heappush(min_heap, (node_time + neighbor_time, neighbor))

        return curr_max_time if len(visit) == n else -1
      
      
# Time Complexity: O(E log V)
# Adjacency List:
# adj_map = collections.defaultdict(list)
# for start, end, time in times:
# adj_map[start].append((end, time))
# This loop runs once for every edge.
# Complexity: O(E)
# Dijkstra's Algorithm (Main Loop):
# while min_heap:
# The while loop processes each node and its edges. In the worst case, every node is pushed onto the heap.
# heapq.heappop(min_heap): This operation runs for each node that is visited. The heap can store up to V nodes. The complexity of heappop is O(log V). Therefore, the total time for all heappop operations is O(V log V).
# heapq.heappush(min_heap, ...): In the worst case, we might push an entry onto the heap for every edge in the graph. The complexity of heappush is O(log V). Therefore, the total time for all heappush operations is O(E log V).
# Overall Time Complexity:
# The total time complexity is dominated by the heap operations within the loops.
# Combining the parts: O(E) + O(V log V) + O(E log V).
# Since in a connected graph E is typically greater than or equal to V-1, the O(E log V) term dominates.
# Final Time Complexity: O(E log V)
# Space Complexity: O(V + E)
# Adjacency List (adj_map):
# Stores every edge in the graph.
# Space: O(E)
# Min-Heap (min_heap):
# In the worst-case scenario, the heap could store an entry for every node.
# Space: O(V)
# Visited Set (visit):
# Stores each visited node once.
# Space: O(V)
# Overall Space Complexity:
# The total space is the sum of the space used by these data structures.
# O(E) + O(V) + O(V) = O(E + 2V)
# Final Space Complexity: O(V + E)