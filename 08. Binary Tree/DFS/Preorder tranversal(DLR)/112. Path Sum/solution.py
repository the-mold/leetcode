class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(node, target):
            if not node:
                return False
            
            is_leaf_node = not node.left and not node.right
            if target - node.val == 0 and is_leaf_node:
                return True
            
            left = helper(node.left, target - node.val)
            right = helper(node.right, target - node.val)

            return left or right

        return helper(root, targetSum)

#T:O(n), because each node is visited once.

# Space Complexity: O(h)
# Where h is the height of the tree (due to recursion stack).

# Best case (balanced tree): O(log n)
# Worst case (skewed tree): O(n)
