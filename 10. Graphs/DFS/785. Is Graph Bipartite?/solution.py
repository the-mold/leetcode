class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colored = {}
        adj_map = {}
        for idx, val in enumerate(graph):
            adj_map[idx] = val

        for node in adj_map:
            if node in colored:
                continue

            if self._isBipartite(adj_map, node, colored, True) == False:
                return False

        return True

    def _isBipartite(self, adj_map, node, colored, curr_color):
        if node in colored:
            return colored[node] == curr_color

        colored[node] = curr_color
        for neighbor in adj_map[node]:
            if self._isBipartite(adj_map, neighbor, colored, not curr_color) == False:
                return False

        return True
      
# Let n is the number of nodes  
      
# T:O(n**n) or O(number of edges)
# S:O(n)