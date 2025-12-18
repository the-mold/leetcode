# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = self._get_path(root, p)
        path2 = self._get_path(root, q)

        # reverse the order
        path1 = path1[::-1]
        path2 = path2[::-1]

        short_path = None
        if len(path1) < len(path2):
            short_path = path1
        else:
            short_path = path2
        
        # find the first element in path that is different
        for i in range(len(short_path)):
            if path1[i].val != path2[i].val:
                return path1[i-1]

        return short_path[-1]

    def _get_path(self, node, target):
        if not node:
            return False
        if node.val == target.val:
            return [node]

        left = self._get_path(node.left, target)
        if left:
            left.append(node)
            return left

        right = self._get_path(node.right, target)
        if right:
            right.append(node)
            return right

        return None

# T:O(n)
# S:O(n)
