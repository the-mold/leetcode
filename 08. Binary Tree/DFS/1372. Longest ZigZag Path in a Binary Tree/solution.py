# Definition for a binary tree node.
# You would be given this class definition in a coding platform like LeetCode.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        """
        Calculates the length of the longest ZigZag path in a binary tree.
        """
        # This variable will store the maximum length found during the traversal.
        # We use a list or a mutable object to allow modification within the nested function.
        self.max_length = 0

        def dfs(node, direction, length):
            """
            Performs a depth-first search to find the longest zigzag path.
            
            :param node: The current node in the tree.
            :param direction: The direction of the move that led to this node ('L' or 'R').
            :param length: The length of the zigzag path ending at this node.
            """
            if not node:
                return

            # The length of the path ending at the current node is a potential maximum.
            self.max_length = max(self.max_length, length)

            # If the last move was to the LEFT:
            if direction == 'L':
                # To continue the zigzag, we must now go RIGHT. The path length increases by 1.
                dfs(node.right, 'R', length + 1)
                # We can also start a NEW zigzag path by going LEFT again. This new path has length 1.
                dfs(node.left, 'L', 1)
            
            # If the last move was to the RIGHT:
            elif direction == 'R':
                # To continue the zigzag, we must now go LEFT. The path length increases by 1.
                dfs(node.left, 'L', length + 1)
                # We can also start a NEW zigzag path by going RIGHT again. This new path has length 1.
                dfs(node.right, 'R', 1)

        # Start the DFS from the root. We can initiate a path by going
        # left or right from the root. These initial moves start a path of length 1.
        # A single node has a path length of 0, so we start the recursion from the children.
        dfs(root.left, 'L', 1)
        dfs(root.right, 'R', 1)
        
        return self.max_length


# Time Complexity: O(N)
# The time complexity is O(N) because the algorithm must visit every node in the tree exactly once to determine the longest path.

# The dfs function is called for each node.
# Inside the function, all operations (comparisons, assignments, and making the next recursive calls) take constant time, O(1).
# Since we process each of the N nodes once, the total time taken is directly proportional to the number of nodes.
# Therefore, the time complexity is O(N).

# Space Complexity: O(H)
# The space complexity is O(H), which is determined by the maximum depth of the recursion stack.

# The algorithm uses recursion (dfs calls itself), and each call adds a new frame to the call stack.
# The maximum number of frames on the stack at any one time corresponds to the longest path from the root to a leaf node, which is the height (H) of the tree.
# This means:

# Best/Average Case (Balanced Tree): If the tree is well-balanced, the height H is approximately log(N). The space complexity would be O(log N).
# Worst Case (Skewed Tree): If the tree is completely unbalanced (like a linked list), the height H is N. The space complexity would be O(N).


# Tranverse - preorder traversal
# The key pattern is Process Node, then Traverse Children. The very first thing the function does after the base case check is process the current node by updating self.max_length. Only after that does it make recursive calls to its children.

# This matches the definition of a preorder traversal:

# Visit/Process the current node.
# Traverse the left subtree.
# Traverse the right subtree.
# Even though the order of visiting left and right children depends on the direction, the fundamental step of processing the node before its descendants remains consistent, making it a preorder traversal.
