# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        """
        The main function that initiates the search. It traverses every node
        and uses each one as a potential starting point for a path.
        """
        # If the tree is empty, no paths exist.
        if not root:
            return 0
        
        # 1. Count paths that start at the current root node.
        paths_starting_at_root = self.count_paths_from_node(root, targetSum)
        
        # 2. Recursively count paths in the left subtree (that don't include the root).
        paths_in_left_subtree = self.pathSum(root.left, targetSum)
        
        # 3. Recursively count paths in the right subtree (that don't include the root).
        paths_in_right_subtree = self.pathSum(root.right, targetSum)
        
        # The total is the sum of all three.
        return paths_starting_at_root + paths_in_left_subtree + paths_in_right_subtree

    def count_paths_from_node(self, node, remaining_sum: int) -> int:
        """
        Helper function: Counts valid paths that start from a specific 'node'.
        """
        # Base case: If we've reached a null node, this path is invalid.
        if not node:
            return 0
            
        count = 0
        
        # Check if the current node's value completes the path.
        if node.val == remaining_sum:
            count += 1
            
        # Continue searching down the left and right children.
        # The new target sum is the remaining sum minus the current node's value.
        count += self.count_paths_from_node(node.left, remaining_sum - node.val)
        count += self.count_paths_from_node(node.right, remaining_sum - node.val)
        
        return count
  
    
# The Simple Approach: Double Traversal
# The idea is to break the problem into two parts:

# A main function that traverses every node in the tree. Let's call the current node start_node.
# For each start_node, we'll use a helper function to do a second traversal downwards, calculating all path sums that begin at that start_node.
# This way, we systematically check every possible path.

# Step-by-step logic:

# pathSum(root, targetSum) (Main Function):
# If the tree is empty (root is None), there are no paths, so return 0.
# The total number of paths in the whole tree is the sum of three values:
# The number of paths that start at the current root and sum to targetSum.
# The number of paths that exist entirely within the left subtree.
# The number of paths that exist entirely within the right subtree.
# We find these three values and add them up. The first is calculated by a helper function, and the other two are found by calling pathSum recursively on the children.
# count_paths_from_node(node, remaining_sum) (Helper Function):
# This function's job is to count how many paths starting from node equal remaining_sum.
# If the node is None, we've gone off the path, so return 0.
# Check if the current node.val is equal to the remaining_sum. If it is, we've found one valid path.
# Recursively call the helper for the left and right children, but this time, the target sum is remaining_sum - node.val.
# The total count is the sum of paths found at the current node plus those found in its children.