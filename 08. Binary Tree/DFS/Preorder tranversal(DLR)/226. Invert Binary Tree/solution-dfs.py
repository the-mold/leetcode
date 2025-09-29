# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return
          
            node.left, node.right = node.right, node.left
            dfs(node.left)
            dfs(node.right)
          
        dfs(root)

        return root

# Time Complexity: O(n)
# The function visits each node in the tree exactly once.
# Let n be the number of nodes in the tree. The work done at each node is constant time (a single swap operation).
# Therefore, the total time complexity is directly proportional to the number of nodes, resulting in O(n).

# Space Complexity: O(h)
# The space complexity is determined by the maximum depth of the recursion stack.
# In the worst-case scenario (a skewed tree, where each node has only one child), the recursion depth will be equal to the number of nodes, n. So, the space complexity would be O(n).
# In the best-case scenario (a balanced binary tree), the height h of the tree is log(n). The space complexity would be O(log n).
# Therefore, the space complexity is O(h), where h is the height of the tree.

# Traversal
# The traversal used in the invertTree solution is a pre-order traversal.

# Let's break down why. The order of operations within the dfs function is:

# Process the current node: node.left, node.right = node.right, node.left
# Recurse on the left child: dfs(node.left)
# Recurse on the right child: dfs(node.right)
# This "Data -> Left -> Right" pattern is the definition of a pre-order traversal.