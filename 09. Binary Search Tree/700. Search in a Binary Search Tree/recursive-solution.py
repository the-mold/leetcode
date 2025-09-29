class SolutionRecursive:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base Cases:
        # 1. If the tree is empty or
        # 2. If the current node's value is the one we're looking for.
        if root is None or root.val == val:
            return root
        
        # Recursive Step:
        # If the target value is smaller, search in the left subtree.
        if val < root.val:
            return self.searchBST(root.left, val)
        # Otherwise, search in the right subtree.
        else:
            return self.searchBST(root.right, val)
        
# Time Complexity: O(H), where H is the height of the tree.
# In a balanced BST, the height is log(n), so the complexity is O(log n).
# In the worst case (a skewed tree, like a linked list), the height is n, so the complexity is O(n).

# Space Complexity
# Iterative Solution: O(1). We only use a single pointer (current_node), so the space is constant.
# Recursive Solution: O(H). The space is determined by the maximum depth of the recursion stack, which is the height of the tree.
