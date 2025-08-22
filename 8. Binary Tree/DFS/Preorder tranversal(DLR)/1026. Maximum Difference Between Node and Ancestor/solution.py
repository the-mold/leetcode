# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.max_diff = 0

        def helper(node, curr_min, curr_max):
            if not node:
                return None

            self.max_diff = max(self.max_diff, abs(curr_min-node.val), abs(curr_max - node.val))

            curr_min = min(curr_min, node.val)
            curr_max = max(curr_max, node.val)

            helper(node.left, curr_min, curr_max)
            helper(node.right, curr_min, curr_max)
        
        helper(root, root.val, root.val)

        return self.max_diff


# Time complexity: O(N) since we visit all nodes once.
# Space complexity: O(N) since we need stacks to do recursion, and the maximum depth of the recursion is the height of the tree, which is O(N) in the worst case and O(log(N)) in the best case.
