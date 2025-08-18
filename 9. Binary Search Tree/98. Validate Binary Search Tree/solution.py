# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return is_valid(root, float("-inf"), float("inf"))
    
    def is_valid(self, node, low, high):
        if not node:
            return True
        
        if node.val <= low or node.val >= high:
            return False
        
        return self.is_valid(node.left, low, node.val) and self.is_valid(node.right, node.val, high)
    
# T:O(n)
# S:O(n)