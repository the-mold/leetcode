class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adjecency_map = collections.defaultdict(list)

        for idx, edges in enumerate(graph):
            if not edges:
                continue
            adjecency_map[idx] = edges

        res = []

        source = 0
        destination = len(graph) - 1

        def dfs(node, curr_path):
            curr_path.append(node)

            if node == destination:
                res.append(list(curr_path))

            for neighbour in adjecency_map[node]:
                dfs(neighbour, curr_path)

            curr_path.pop()


        dfs(source, [])
        return res