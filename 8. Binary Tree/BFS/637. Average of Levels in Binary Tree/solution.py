# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            queue_size = len(queue)
            queue_sum = 0

            for i in range(queue_size):
                node = queue.pop(0)
                queue_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(queue_sum / queue_size)
        
        return res

# Time Complexity: O(N^2) in the worst case, where N is the number of nodes.
# Why? While we still visit each node and its children only once (which seems like O(N) work), the operation queue.pop(0) on a Python list is expensive. To remove the first element from a list, Python must shift all subsequent elements one position to the left. This operation takes time proportional to the number of elements in the list.
# In the worst-case scenario (a wide, complete binary tree), the last level can contain up to N/2 nodes. When processing this level, each pop(0) operation could take up to O(N) time. Since we do this for all N/2 nodes on that level, the total time for that level alone can approach O(N^2).
# This is the key difference from the collections.deque version, where popleft() is an O(1) operation, making the total time complexity a much more efficient O(N).
# Space Complexity: O(W), where W is the maximum width of the tree.
# This remains unchanged. The space is dominated by the maximum number of nodes stored in the queue at any given time, which corresponds to the widest level of the tree.
