# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _generateTrees(self, start, end, memo):
        key = (start, end)
        if key in memo:
            return memo[key]

        # When start > end, there are no valid values in range, so return a list containing one empty subtree (None).
        if start > end:
            return [None]

        res = []

        # try all possible root values
        for i in range(start, end + 1):
            # contains all possible BST structures for values < root
            left = self._generateTrees(start, i - 1, memo)
            # contains all possible BST structures for values > root
            right = self._generateTrees(i + 1, end, memo)

            for leftSubtree in left:
                for rightSubtree in right:
                    root = TreeNode(i, leftSubtree, rightSubtree)
                    res.append(root)
            
        memo[key] = res
        return memo[key]

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self._generateTrees(1, n, {})
      
# Example Walkthrough (n=3)
# For generateTrees(3) → _generateTrees(1, 3, {}):

# When i=1 (root=1):

# left = _generateTrees(1, 0, {}) → [None] (empty left)
# right = _generateTrees(2, 3, {}) → generates all BSTs with nodes 2,3
# Combines: 1 left option × multiple right options = multiple trees
# When i=2 (root=2):

# left = _generateTrees(1, 1, {}) → [TreeNode(1)]
# right = _generateTrees(3, 3, {}) → [TreeNode(3)]
# Combines: 1 left × 1 right = 1 tree
# When i=3 (root=3):

# left = _generateTrees(1, 2, {}) → generates all BSTs with nodes 1,2
# right = _generateTrees(4, 3, {}) → [None] (empty right)
# Combines: multiple left options × 1 right option = multiple trees



# Time Complexity Analysis
# The time complexity is O(4^n / √n), which is the n-th Catalan number.

# Space Complexity Analysis
# The space complexity is also O(4^n / √n).