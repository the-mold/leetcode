class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Finds the lowest common ancestor of two nodes in a binary tree.

        :param root: The root of the binary tree.
        :param p: The first node.
        :param q: The second node.
        :return: The lowest common ancestor node.
        """
        # Base case: if the root is None, or if the root is one of the nodes,
        # then the root is the LCA.
        if not root or root == p or root == q:
            return root

        # Recurse on the left and right subtrees
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right subtrees return a non-None value,
        # it means p and q are in different subtrees, so the current root is the LCA.
        if left_lca and right_lca:
            return root

        # Otherwise, the LCA is in either the left or the right subtree.
        # If one of them is None, the other one is the result.
        return left_lca if left_lca is not None else right_lca
    
# The Logic
# The core idea is to use a recursive approach. We'll traverse the tree from the root downwards. For any given node, we'll check three conditions:

# Is the current node one of the nodes we're looking for (p or q)?
# Can we find p or q in the left subtree?
# Can we find p or q in the right subtree?
# The LCA is the first node where one of the target nodes is found in 
# its left subtree and the other is in its right subtree. An interesting 
# edge case is when one of the nodes is an ancestor of the other. In that 
# situation, the ancestor node is the LCA. Our recursive solution handles this gracefully.
