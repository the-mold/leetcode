# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None

        parent_val = preorder[0]
        node = TreeNode(parent_val)
        mid = inorder.index(parent_val)

        in_left = inorder[:mid]
        in_right = inorder[mid+1:]
        pre_left = preorder[1:1+len(in_left)]
        pre_right = preorder[1 + len(in_left):]

        node.left = self.buildTree(pre_left, in_left)
        node.right = self.buildTree(pre_right, in_right)

        return node
      
# T:O(n**2)
# S:O(n**2)
