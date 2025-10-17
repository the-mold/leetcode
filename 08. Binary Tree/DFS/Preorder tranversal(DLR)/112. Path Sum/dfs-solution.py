# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, target):
            if not node:
                return False

            # return true if it is a leaf node and value is equal to remainder
            if not node.left and not node.right:
                return node.val == target

            target = target - node.val
            return dfs(node.left, target) or dfs(node.right, target)
        
        return dfs(root, targetSum)