class Solution:
    def findCircleNum(self, isConnected):
        number_of_nodes = len(isConnected)
        visited = [False] * number_of_nodes
        connected_region = 0

        def dfs(node_idx):
            visited[node_idx] = True
            for neighbour_node_idx in range(number_of_nodes):
                if isConnected[node_idx][neighbour_node_idx] == 1 and not visited[neighbour_node_idx]:
                    dfs(neighbour_node_idx)

        for node_idx in range(number_of_nodes):
            if not visited[node_idx]:
                connected_region += 1       # if you find an unvisited node, it means it is a new interconnected node region. The dfs function in next line makes sure that all other nodes connected to this node are visited and they form a province. You will mark all visited nodes in `visited` array and will not come back to them again. So you come to this line only when you really discover an unseen node region.
                dfs(node_idx)
        
        return connected_region

# Complexity Analysis
# Here n is the number of cities.

# Time complexity: O(n^2).
# Initializing the visit array takes O(n) time.
# The dfs function visits each node once, which takes O(n) time because there are n nodes in total. From each node, we iterate over all
# possible edges using isConnected[node] which takes O(n) time for each visited node. As a result, it takes a total of O(n^2) time to 
# visit all the nodes and iterate over its edges.

# Space complexity: O(n).
# The visit array takes O(n) space.
# The recursion call stack used by dfs can have no more than n elements in the worst-case scenario. It would take up O(n) space in that case.


# NOTE: Problem could also be solved with `Union find` algorythm that is basically created for this type of problems.