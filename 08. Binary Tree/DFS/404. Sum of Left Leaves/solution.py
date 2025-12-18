# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(node, is_left):
            if not node:
                return 0

            left = helper(node.left, True)
            right = helper(node.right, False)

            node_value = 0
            is_leaf = not node.left and not node.right
            if is_left and is_leaf:
                node_value = node.val

            return node_value + left + right

        return helper(root, False)

