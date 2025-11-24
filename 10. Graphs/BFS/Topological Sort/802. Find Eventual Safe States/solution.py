# Core Idea (BFS on Reverse Graph)
# A node is safe if all paths from it lead to a terminal node.
# Let's reverse the logic: A node is safe if we can reach it by starting from a terminal node and traversing the graph's edges backwards.
# Terminal nodes are our initial "safe" nodes. Any node whose outgoing edges only lead to already-known safe nodes is also safe.


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        # We need to know "who points to me?" to work backwards.
        reverse_graph = defaultdict(list)

        # We also need the out-degree of each node in the ORIGINAL graph.
        # An out-degree of 0 means it's a terminal node.
        out_degree = [0] * n

        for idx, nodes in enumerate(graph):
            for node in nodes:
                # In the reverse graph, an edge from i -> neighbor becomes neighbor -> i.
                reverse_graph[node].append(idx)
                out_degree[idx] += 1

        q = collections.deque()
        for node_id, val in enumerate(out_degree):
            if val == 0:
                q.append(node_id)

        while q:
            curr_node = q.popleft()

            for node in reverse_graph[curr_node]:
                out_degree[node] -= 1
                if out_degree[node] == 0:
                    q.append(node)
        
        
        return [idx for idx, val in enumerate(out_degree) if val == 0]
      
# T:O(V+E)
# S:O(V+E)