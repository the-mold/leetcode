
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = [root]

        while q:
            q_length = len(q)
            level_nodes = []

            for i in range(q_length):           #O(n)
                node = q.pop(0)                 #O(n)

                level_nodes.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            right_node = level_nodes.pop()        #O(1)
            res.append(right_node)
        
        return res
    
# Complexity Analysis
# Time Complexity: O(N^2) in the worst case, where N is the total number of nodes.
# Reasoning: The core of the algorithm is a level-order traversal. The outer while loop runs once per level, and the inner for loop ensures that every node is processed exactly once.
# The bottleneck, once again, is the operation q.pop(0). Because q is a standard Python list, removing an element from the beginning is an O(k) operation, where k is the current length of the list. This is because all subsequent elements must be shifted forward.
# In a wide, bushy tree (like a complete binary tree), the queue can become very large, holding up to roughly N/2 nodes. When processing the level just before the widest level, each pop(0) call becomes very slow, leading to a total time complexity that is quadratic in the number of nodes.
# Space Complexity: O(W), where W is the maximum width of the tree.
# Reasoning: The auxiliary space is dominated by two data structures:
# The queue q: It stores nodes for the current and next levels. Its maximum size is proportional to the maximum number of nodes at any single level, which is the width (W) of the tree.
# The list level_nodes: This list also stores all nodes on the current level, so its maximum size is also W.
# Since both structures are bounded by the tree's maximum width, the overall space complexity is O(W). For a complete binary tree, W can be up to O(N), making the worst-case space complexity O(N). The res list stores H elements (where H is the height), which is typically less than W.
# Optimization Note: Just like in the previous examples, you could significantly improve the performance by using collections.deque. Replacing q = [root] with q = collections.deque([root]) and q.pop(0) with q.popleft() would make the dequeue operation O(1), reducing the overall time complexity to an optimal O(N).
