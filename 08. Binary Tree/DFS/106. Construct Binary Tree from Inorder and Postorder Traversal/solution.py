# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        value = postorder[-1]
        in_value_idx = inorder.index(value)
        node = TreeNode(value)

        in_left = inorder[:in_value_idx]
        in_right = inorder[in_value_idx+1:]
        post_left = postorder[:in_value_idx]
        post_right = postorder[in_value_idx:len(postorder)-1]

        node.left = self.buildTree(in_left, post_left)
        node.right = self.buildTree(in_right, post_right)

        return node
      
# T:O(n**2)
# S:O(n**2)