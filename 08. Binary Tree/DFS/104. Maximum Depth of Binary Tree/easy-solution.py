# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0

        def dfs(node, depth):
            if not node:
                return depth

            depth += 1

            self.max_depth = max(self.max_depth, depth)

            dfs(node.left, depth)
            dfs(node.right, depth)


        dfs(root, 0)

        return self.max_depth