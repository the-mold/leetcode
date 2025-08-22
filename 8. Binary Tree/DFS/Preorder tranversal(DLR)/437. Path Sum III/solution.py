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
            paths_found = 1 if currentSum == targetSum else 0
            paths_found += countPathFromNode(node.left, currentSum)
            paths_found += countPathFromNode(node.right, currentSum)

            return paths_found

        if not root:
            return 0

        #count paths from current node
        pathsFromRoot = countPathFromNode(root, 0)

        # do the same for left and right children. This is how you trigger function for every node in the tree. First do smth for root, then for left and right start the main function again.
        pathsFromLeft = self.pathSum(root.left, targetSum)
        pathsFromRight = self.pathSum(root.right, targetSum)

        return pathsFromRoot + pathsFromLeft + pathsFromRight
    
#T: O(n^2) , calculate path for each node separately
# 1.Main function pathSum(): Visits every node once → O(n)
# 2.For each node: Calls pathsFromCurrentNode() → O(h) in average case, O(n) in worst case
# 3.Total: O(n) × O(n) = O(n²) worst case
                       
#S: O(n)

#Tranverse - preorder