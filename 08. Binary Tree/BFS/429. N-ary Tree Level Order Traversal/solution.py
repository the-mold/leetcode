"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        q = collections.deque()
        q.append(root)
        res = []

        while q:
            level_nodes = len(q)
            curr_nodes = []
            for _ in range(level_nodes):
                node = q.popleft()
                if not node:
                    continue

                curr_nodes.append(node.val)
                if node.children:
                    for child in node.children:
                        q.append(child)
            
            res.append(curr_nodes)
        
        return res

# T:O(N), we visit all nodes once.
# S:O(W), where W is maximum width of the tree