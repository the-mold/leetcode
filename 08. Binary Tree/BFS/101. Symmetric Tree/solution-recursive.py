# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root, root)
    
    def isMirror(self, n1, n2):
        if not n1 and not n2: 
            return True
        if not n1 or not n2:
            return False
        
        return (
            n1.val == n2.val
            and self.isMirror(n1.left, n2.right)
            and self.isMirror(n1.right, n2.left)
        )

# Time complexity: O(n). Because we traverse the entire input tree once, the total run time is O(n), where n is the total number of nodes in the tree.

# Space complexity: The number of recursive calls is bound by the height of the tree. In the worst case, the tree is linear and the height is in O(n). Therefore, space complexity due to recursive calls on the stack is O(n) in the worst case.
