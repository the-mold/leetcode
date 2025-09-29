from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Finds a node with the given value in a BST using an iterative approach.
        """
        # Start at the root of the tree.
        current_node = root
        
        # Loop until we either find the value or run out of nodes to check.
        while current_node is not None:
            # If we found the value, return the node (and its subtree).
            if val == current_node.val:
                return current_node
            
            # If the target value is smaller, go left.
            elif val < current_node.val:
                current_node = current_node.left
            
            # If the target value is larger, go right.
            else: # val > current_node.val
                current_node = current_node.right
                
        # If the loop completes, the value was not in the tree.
        return None
              

# Time Complexity: O(H), where H is the height of the tree.
# In a balanced BST, the height is log(n), so the complexity is O(log n).
# In the worst case (a skewed tree, like a linked list), the height is n, so the complexity is O(n).
# Space Complexity:
# Iterative Solution: O(1). We only use a single pointer (current_node), so the space is constant.