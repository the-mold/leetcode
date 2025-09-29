# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = [root]
        ans = []
        level = 0

        while q:
            level_size = len(q)
            level_nodes = []

            for i in range(level_size):
                node = q.pop(0)
                level_nodes.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if level % 2 == 1:
                level_nodes.reverse()

            ans.append(level_nodes)
            level +=1 

        return ans

# T:O(n**2), algorithm visits each node only once, hence O(n). Additional n comes from .pop(0) operation. 
# S:O(n)
