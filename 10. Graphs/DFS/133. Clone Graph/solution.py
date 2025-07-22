"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.cloned_nodes = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        
        if node in self.cloned_nodes:
            return self.cloned_nodes[node]

        cloned_node = Node(node.val)

        self.cloned_nodes[node] = cloned_node

        if node.neighbors:
            cloned_node.neighbors = [self.cloneGraph(neighbour) for neighbour in node.neighbors]
        
        return cloned_node
    
#T:O(n)
#S:O(n)