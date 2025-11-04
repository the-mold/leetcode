import collections
import heapq
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj_map = collections.defaultdict(list)
        for i, (start, end) in enumerate(edges):
            prob = succProb[i]
            adj_map[start].append((end, prob))
            adj_map[end].append((start, prob))

        # max_prob[i] will store the maximum probability to reach node i from start_node.
        max_prob = [0.0] * n
        max_prob[start_node] = 1.0 # The probability to reach the start node from itself is 1.

        # A max-priority queue storing tuples of (-probability, node).
        # We use a min-heap, so negative probabilities simulate a max-heap.
        heap = [(-1.0, start_node)]

        while heap:
            curr_probability, node = heapq.heappop(heap)
            curr_probability = -curr_probability

            # If the probability of the path we just popped is less than the
            # best probability we've already found for this node, it's a stale
            # entry from the heap. We can safely ignore it and continue.
            if curr_probability < max_prob[node]:
                continue

            # If we've reached the end node, we can return. Because we always
            # explore the path with the highest probability first (thanks to the
            # max-heap), the first time we reach the end node is guaranteed to be
            # via the most probable path.
            if node == end_node:
                return curr_probability
            
            # Explore neighbors of the current node.
            for (neighbour_node, prob) in adj_map[node]:
                # Calculate the probability of the path through the current node to the neighbor.
                new_prob = curr_probability * prob

                # If this new path is more probable than any path we've found to
                # the neighbor so far, update it and add the new path to the heap.
                if new_prob > max_prob[neighbour_node]:
                    max_prob[neighbour_node] = new_prob
                    heapq.heappush(heap, (-new_prob, neighbour_node))
        
        # If the loop finishes and we haven't returned, it means the end_node was
        # never reached.
        return 0.0
  
# Let:
# V be the number of nodes (n).
# E be the number of edges (len(edges)).

# Time Complexity: O(E log V)
# Building the Adjacency List (adj_map):
# The code iterates through the edges list once.
# This takes O(E) time.
# Initialization:
# Creating the max_prob array of size n takes O(V) time.
# Initializing the heap is O(1).
# Main Loop (Dijkstra's Algorithm):
# The while loop runs as long as there are items in the heap.
# In the worst case, every edge can result in a heapq.heappush operation. The size of the heap can grow up to E.
# heapq.heappop(heap): The cost of extracting the minimum element from the heap is O(log(heap_size)). Since the heap size can be at most E, this is O(log E). This operation can be called up to E times in the worst case.
# heapq.heappush(heap, ...): The cost of adding an element to the heap is also O(log E). This is done for each edge of a processed node if a better path is found.
# The total complexity of the loop is dominated by the heap operations. Over the entire execution, there will be at most E pushes and E pops.
# Therefore, the complexity of the main loop is O(E log E).
# Refining the Complexity:
# In a simple graph, the number of edges E can be at most V * (V - 1). This means log E can be up to log(V^2), which is 2 * log V. So, O(log E) is equivalent to O(log V).
# By substituting log V for log E, the time complexity becomes O(E log V). This is the standard complexity for Dijkstra's algorithm implemented with a binary heap when applied to a graph that is not necessarily sparse.
# Final Time Complexity: O(E log V)

# Space Complexity: O(V + E)
# Adjacency List (adj_map):
# This stores the entire graph. Since each edge is stored twice (for the undirected graph), it holds 2 * E entries.
# Space: O(E)
# max_prob Array:
# This array stores the maximum probability for each of the V nodes.
# Space: O(V)
# Heap (heap):
# In the worst-case scenario, the heap could contain an entry for every edge if many paths are explored.
# Space: O(E)
# Combining these, the total space complexity is O(E) + O(V) + O(E), which simplifies to:

# Final Space Complexity: O(V + E)