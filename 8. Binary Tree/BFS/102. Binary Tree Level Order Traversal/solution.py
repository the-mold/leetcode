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
#S: O(W)

# Time Complexity: O(N^2) in the worst case, where N is the total number of nodes in the tree.
# Reasoning: The algorithm iterates through each node of the tree exactly once. However, the choice of data structure for the queue is critical. The code uses a standard Python list and the operation queue.pop(0) to remove the element from the front.
# On a list, pop(0) is an expensive operation. It has a time complexity of O(k), where k is the number of elements in the list, because all subsequent elements must be shifted to the left.
# In a wide, bushy tree, the queue can hold many nodes at once (up to the maximum width of the tree, which can be as large as N/2). When the queue is at its largest, each pop(0) operation becomes very slow.
# In the worst-case scenario of a complete binary tree, the work done processing the level before the last one involves many pop(0) calls on a queue containing roughly N/2 elements, leading to a total time complexity that approaches O(N^2).
# Space Complexity: O(W) for auxiliary space, where W is the maximum width of the binary tree.
# Reasoning: The space used by the algorithm is primarily determined by the queue. At any point in time, the queue holds at most all the nodes of one level plus the nodes of the next level that have been added. The maximum number of nodes it will ever hold is proportional to the widest level of the tree (W).
# The current_level list also temporarily stores nodes of a single level, so its space is also bounded by O(W).
# Therefore, the auxiliary space (the space used by the algorithm itself, not including the output) is O(W).
# Note: The result array itself will store all N nodes, so if you include the space required for the output, the total space complexity is O(N).

# Pro Tip: To make this algorithm much more efficient, you could replace the list-based queue with a collections.deque. Using deque.popleft() is an O(1) operation, which would improve the overall time complexity to an optimal O(N).




# Example Usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(Solution().levelOrder(root))