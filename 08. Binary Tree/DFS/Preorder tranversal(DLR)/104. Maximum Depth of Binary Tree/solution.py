# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1

#T:O(n)

#S:O(n)   <--- number of recursive calls
# Worst case Space: (O(n)):
# In a completely skewed tree (like a linked list), the recursion goes deep into one branch, visiting every node with one recursive call at a time.
# → So the call stack grows to n levels → O(n) space.

# Best case Space (O(log n)):
# In a perfectly balanced tree, for each node, we make two recursive calls, and the height of the tree is log n.
# → The call stack depth is at most log n → O(log n) space.
