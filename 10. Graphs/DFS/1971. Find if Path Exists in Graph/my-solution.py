class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        dic = collections.defaultdict(list)

        for start, end in edges:
            dic[start].append(end)
            dic[end].append(start)

        if not dic[source]:
            return False

        seen = set()
        def dfs(node, dic):
            if node == destination:
                return True
            
            seen.add(node)
            node_edges = dic[node]
            for edge in node_edges:
                if not edge in seen:
                    if dfs(edge, dic):
                        return True
            
            return False

        return dfs(source, dic)
