# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return 

            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(nums) - 1)
  
  
# nums = [-10, -3, 0, 5, 9]
#           0   1  2  3  4
            
# Result:
  #     0
  #    / \
  #  -10  5
  #    \   \
  #    -3   9
            
            
# helper(0, 4)
#   mid = 2
#   root = TreeNode(0)
#   root.left = helper(0, 1)
#   root.right = helper(3, 4)
  
#   helper(0,1)
#     mid = 0
#     root = TreeNode(-10)
#     root.left = helper(0, -1) => None
#     root.right = helper(1, 1) => TreeNode(-3)
    
#   helper(3,4)
#     mid = 3
#     root = TreeNode(5)
#     root.left = helper(3, 2) => None 
#     root.right = helper(4, 4) => TreeNode(9)
  
    

    
    
  
# Time Complexity: O(n)
# Each element visited once: The function creates exactly one TreeNode for each element in nums
# Work per node: O(1) - just arithmetic and node creation
# Total: O(1) × n nodes = O(n)
# Space Complexity: O(log n)
# This is the optimized index-based version, so:

# Recursion stack: O(log n) for a balanced tree
# Tree height = log₂(n) for balanced BST
# Maximum recursive calls on stack = tree height
# No extra arrays: Unlike slicing approach, this doesn't create new arrays
# Node storage: O(n) for the tree itself (but this is output, not auxiliary space)