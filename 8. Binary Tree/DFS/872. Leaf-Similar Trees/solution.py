# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def helper(node, leaves):
            if not node:
                return leaves
            
            if not node.left and not node.right:
                leaves.append(node.val)
            
            helper(node.left, leaves)
            helper(node.right, leaves)
        
        leaves1 = []
        leaves2 = []
        helper(root1, leaves1)
        helper(root2, leaves2)

        return leaves1 == leaves2

#T:O(n)
#S:O(n), worst case when there are completely skewed trees
