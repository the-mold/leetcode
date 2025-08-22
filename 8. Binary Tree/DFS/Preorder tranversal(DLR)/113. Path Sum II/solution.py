# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []

        def dfs(node, remainder, nodesOnPath):
            if not node:
                return None
            
            nodesOnPath.append(node.val)

            if not node.left and not node.right and remainder == node.val:
                self.ans.append(list(nodesOnPath))
            else:
                dfs(node.left, remainder - node.val, nodesOnPath)
                dfs(node.right, remainder - node.val, nodesOnPath)
            
            # pop a node after you processed it. Otherwise it appears in list all the time
            nodesOnPath.pop()

        dfs(root, targetSum, [])

        return self.ans
