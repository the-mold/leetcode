# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def countPathFromNode(node, currentSum):
            if not node:
                return 0
            
            currentSum += node.val
            count = 1 if currentSum == targetSum else 0
            count += countPathFromNode(node.left, currentSum)
            count += countPathFromNode(node.right, currentSum)

            return count

        if not root:
            return 0

        #count paths from current node
        pathsFromRoot = countPathFromNode(root, 0)

        # do the same for left and right children
        pathsFromLeft = self.pathSum(root.left, targetSum)
        pathsFromRight = self.pathSum(root.right, targetSum)

        return pathsFromRoot + pathsFromLeft + pathsFromRight
    
#T: O(n^2) , calculate path for each node separately
#S: O(n)

#Tranverse - preorder