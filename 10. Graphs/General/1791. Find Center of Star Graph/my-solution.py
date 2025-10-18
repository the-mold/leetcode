class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dic = collections.defaultdict(list)

        for start, end in edges:
            dic[start].append(end)
            # also add the reverse because the graph is undirected
            dic[end].append(start)
        
        vertices = len(dic.keys())
        for key, values in dic.items():
            if len(values) == vertices - 1:
                return key

        return -1