from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Deletes a node with the given key from the BST using a recursive approach.
        """
        # Base case: if the tree is empty, we're done.
        if not root:
            return None

        # --- Stage 1: Search for the node ---
        if key < root.val:
            # Go left. The recursive call will return the new state of the left subtree.
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # Go right. The recursive call will return the new state of the right subtree.
            root.right = self.deleteNode(root.right, key)
        else:
            # --- Stage 2: Found the node to delete ---

            # Case A: Node has 0 or 1 child (the easy cases)
            if not root.left:
                return root.right  # Replace with right child (or None if no right child)
            if not root.right:
                return root.left   # Replace with left child

            # Case B: Node has two children (the hard case)
            # Find the smallest node in the right subtree (the in-order successor).
            successor = root.right
            while successor.left:
                successor = successor.left
            
            # Replace this node's value with the successor's value.
            root.val = successor.val
            
            # Recursively delete the successor node from the right subtree.
            root.right = self.deleteNode(root.right, successor.val)
            
        return root



# Time Complexity: O(H)
# The overall time complexity is proportional to the height of the tree, H. Here's why:

# Searching for the Node: The initial part of the function (if key < root.val and if key > root.val) traverses down the tree to find the node with the given key. In the worst case, this search operation takes O(H) time, as we move one level down with each recursive call.
# Deleting the Node (once found):
# Case A (0 or 1 child): This is a constant time, O(1), operation. We just rearrange a few pointers.
# Case B (2 children): This is the most time-consuming part.
# First, we find the in-order successor (while successor.left:). This requires traversing down the left spine of the right subtree. This traversal can take up to O(H) time in the worst case.
# Then, we make another recursive call to deleteNode on the right subtree. This second call also takes time proportional to the height of that subtree.
# Since all these operations happen along a single path from the root down into the tree, the dominant factor is the height of the tree.

# Average Case (Balanced Tree): For a reasonably balanced BST, the height H is approximately log(n), where n is the number of nodes. Therefore, the average time complexity is O(log n).
# Worst Case (Skewed Tree): For a completely unbalanced tree (which resembles a linked list), the height H is n. Therefore, the worst-case time complexity is O(n).
# Space Complexity: O(H)
# The space complexity is determined by the maximum depth of the recursion call stack.

# Since our function is recursive, each call adds a new frame to the stack. The maximum number of frames on the stack at any one time will be the height of the tree, H.
# Average Case (Balanced Tree): The recursion depth will be O(log n).
# Worst Case (Skewed Tree): The recursion depth will be O(n).
# Therefore, the space complexity is O(H), which translates to O(log n) on average and O(n) in the worst case.







# The Overall Strategy
# The function works by traversing down the tree to find the node we need to delete. Once it finds the node, it handles the deletion and then "rebuilds" the connections on its way back up the recursion chain.

# Step-by-Step Breakdown
# Let's trace deleteNode(root, key):

# Step 1: Handle the Base Case
# Code: if not root: return None
# Explanation: The very first thing we check is if the tree (or the current subtree we're looking at) is empty. If it is, we can't delete anything, so we simply return None. This stops the recursion.
# Step 2: Search for the Node to Delete
# This is the recursive part of the search. We compare the key we want to delete with the value of the current root node.

# If key < root.val:
# Code: root.left = self.deleteNode(root.left, key)
# Explanation: If the key is smaller than the current node's value, we know the node we want to delete must be in the left subtree. We make a recursive call on the left child. Crucially, whatever deleteNode returns (the new root of the modified left subtree) is assigned back to root.left. This is how the parent's link is updated.
# If key > root.val:
# Code: root.right = self.deleteNode(root.right, key)
# Explanation: This is the mirror image. If the key is larger, it must be in the right subtree. We recursively call on the right child and update root.right with the result.
# Step 3: Found the Node. Now, Delete It.
# If key == root.val:
# Explanation: We've arrived at the node that needs to be deleted. Now we must handle three possibilities for this node's structure.
# Case A: The node has one or zero children.
# Code: if not root.left: return root.right
# Explanation: If the node has no left child, we can simply replace it with its right child. We do this by returning root.right. This right child will be linked up to the parent node in the previous recursive step. If the node has no children at all, root.right is None, and we correctly replace the node with None.
# Code: if not root.right: return root.left
# Explanation: Similarly, if there's no right child, we replace the node with its left child by returning root.left.
# Case B: The node has two children. (This is the most complex case).
# Explanation: We can't just remove the node, as that would leave two orphaned subtrees. We need to find a replacement node that maintains the BST property. The two valid choices are:
# The largest node in the left subtree.
# The smallest node in the right subtree (the "in-order successor").
# Our solution uses the second option.
# 1. Find the Successor:
# Code: successor = root.right; while successor.left: successor = successor.left
# Explanation: We find the smallest value in the right subtree by going right once, and then as far left as possible.
# 2. Replace the Value:
# Code: root.val = successor.val
# Explanation: We don't move the node itself. We just copy the successor's value into the node we intended to delete. Now our tree is valid, but we have a duplicate value.
# 3. Delete the Duplicate Successor:
# Code: root.right = self.deleteNode(root.right, successor.val)
# Explanation: We make one final recursive call to delete the successor node (which we just copied) from the right subtree. This call is guaranteed to be a simpler case (Case A), because the successor by definition has no left child.
# Step 4: Return the (Potentially Modified) Root
# Code: return root
# Explanation: After the search and potential deletion logic is complete, the function returns the root of the current subtree. This return value propagates back up the call stack, ensuring each parent node is correctly connected to its (possibly new) children.