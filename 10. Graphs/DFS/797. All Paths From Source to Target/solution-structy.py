class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adjecency_map = collections.defaultdict(list)

        for idx, edges in enumerate(graph):
            if not edges:
                continue
            adjecency_map[idx] = edges

        src = 0
        dst = len(graph) - 1

        return [path[::-1] for path in self._allPathsSourceTarget(adjecency_map, src, dst)]

    def _allPathsSourceTarget(self, adj_map, src, dst):
        if src == dst:
            return [[dst]]

        res = []
        for neighbor in adj_map[src]:
            for path in self._allPathsSourceTarget(adj_map, neighbor, dst):
                path.append(src)
                res.append(path)

        return res

# T: O(n * 2**n)
# S: O(n * 2**n)