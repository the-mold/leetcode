# Intuition: for each node check if the left and right heights differ by maximum 1. Otherwise tree is not balanced.

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self._isBalanced(root) > -1

    def _isBalanced(self, node):
        if not node:
            return 0

        left = self._isBalanced(node.left)
        if left == -1:
            return -1

        right = self._isBalanced(node.right)
        if right == - 1:
            return -1

        if abs(left-right) > 1:
            # tree is not balanced! Return to the top of recursion.
            return -1

        # continue recursion. Add current node to the max height of left and right to get the total height so far.
        return 1 + max(left, right)
    
# T:O(n)
# S:O(n)
