# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        res = []
        def backtracking(node, current_combination = "", separator = "->"):
            if not separator:
                separator = ""

            current_combination = f"{current_combination}{separator}{node.val}"

            if not node.left and not node.right:
                res.append(current_combination)
                return
            
            if node.left:
                backtracking(node.left, current_combination)

            if node.right:
                backtracking(node.right, current_combination)

        backtracking(root, "", None)

        return res
    

# Time Complexity: O(N)
# The time complexity is O(N) because the algorithm must visit every node in the tree exactly once.

# Here's a more detailed breakdown of why it's not higher, despite the string concatenations:

# Traversal: The core of the algorithm is a Depth-First Search (DFS). In a DFS traversal of a tree, each node is visited and processed a constant number of times. This gives us a baseline of O(N).
# Path Building: At each node, we append its value to the current_path. While a single string concatenation can be expensive, we can analyze the total work done across all recursive calls. Each node's value is added to a path string exactly once as we traverse down the tree.
# Total Work: Every node and every edge is traversed once. The work done at each node is proportional to the length of the node's value (which we can consider constant). Therefore, the total time taken is proportional to the number of nodes in the tree.
# In some analyses, you might see O(N*H) if string copying is inefficient. However, in a typical analysis of this specific problem, since we are simply building up the path representations during a standard traversal, the complexity is considered linear to the number of nodes.

# Space Complexity: O(H) or O(N) in the worst case
# The space complexity is determined by the maximum depth of the recursion call stack.

# Recursion Stack: The find_paths function calls itself recursively. The maximum number of calls that can be on the stack at any one time is equal to the height of the tree, H. Each call on the stack stores information like the current node and the path string.
# Balanced Tree (Best Case): If the tree is well-balanced, its height H is approximately log(N). In this case, the space complexity would be O(log N).
# Skewed Tree (Worst Case): If the tree is completely unbalanced (like a linked list), its height H is equal to the number of nodes, N. In this scenario, the space complexity becomes O(N).