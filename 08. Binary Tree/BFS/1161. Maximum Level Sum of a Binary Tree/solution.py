# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        q = [root]
        current_level = 0
        max_sum = float("-inf")
        max_level = 0

        while q:
            q_length = len(q)
            level_sum = 0
            current_level += 1

            for i in range(q_length):
                node = q.pop(0)

                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level
        
        return max_level

#T: O(n^2), because of .pop(0)
#S: O(W), where W is max tree width
