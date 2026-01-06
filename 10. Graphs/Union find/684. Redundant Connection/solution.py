class Solution:
    def find(self, roots, node_idx):
        if roots[node_idx] == node_idx:
            return node_idx

        found = self.find(roots, roots[node_idx])
        roots[node_idx] = found
        return found

    def union(self, roots, sizes, a, b):
        root_a = self.find(roots, a)
        root_b = self.find(roots, b)

        if root_a == root_b:
            return False
        
        if sizes[root_a] >= sizes[root_b]:
            roots[root_b] = root_a
            sizes[root_a] += sizes[root_b]
        else:
            roots[root_a] = root_b
            sizes[root_b] += sizes[root_a]

        return True

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = set()
        for a, b in edges:
            nodes.add(a)
            nodes.add(b)
        n = len(nodes)

        roots = [i for i in range(n + 1)]
        sizes = [1 for i in range(n + 1)]

        res = []
        for a, b in edges:
            can_union = self.union(roots, sizes, a, b)
            if not can_union:
                res.append([a, b])

        return res[-1]


# T: O(n + e*α(n)), where α(n) is inverse Ackerman function on n. It is nearly constant. It grows very slowly.
# S:O(n)
