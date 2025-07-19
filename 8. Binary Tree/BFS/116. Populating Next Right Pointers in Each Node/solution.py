"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        q = [root]

        while q:
            q_length = len(q)
            prev_node = None
            curr_node = None

            for i in range(q_length):
                node = q.pop(0)
                curr_node = node

                if prev_node:
                    prev_node.next = curr_node
                
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
                
                prev_node = curr_node
        
        return root
