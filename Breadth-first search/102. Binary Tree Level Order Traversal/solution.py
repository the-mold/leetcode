# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        if not root:
                return []
        
        result = []
        queue = [root]

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.pop(0)  #process queue elements from left to right
                current_level.append(node.val)

                if node.left:
                        queue.append(node.left)
                if node.right:
                        queue.append(node.right)
                
            result.append(current_level)

        return result

#T: O(n^2)      , because .pop() operation is n and the forloop is n so overal complexity is n^2.
#S: O(n)



# Example Usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(Solution().levelOrder(root))