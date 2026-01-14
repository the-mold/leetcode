# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root

        stack = [root]
        prev = None

        while stack:
            node = stack.pop()

            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
            # MIND the Order! if you push left AFTER right it means that left is on top of the stack and will be processed next.
            node.left = None
            node.right = None

            if prev:
                prev.right = node
            prev = node

        return root
      
# T:O(n)
# S:O(n)
