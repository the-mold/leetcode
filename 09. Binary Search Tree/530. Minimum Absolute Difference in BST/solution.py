# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float("inf")
        self.prev = None

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)

            if self.prev:
                self.min_diff = min(self.min_diff, node.val - self.prev.val)
            
            self.prev = node

            dfs(node.right)

        dfs(root)

        return self.min_diff

# T:O(n)
# S:O(W)
# Tranverse: inorder and this is VERY important to get ordered list of nodes. This is property of Binary Search Tree.


# The Problem
# You are given a Binary Search Tree (BST). The task is to find the minimum absolute difference between the values of any two different nodes in the entire tree.

# The Key Insight: BST Property
# The most important property of a Binary Search Tree (BST) for this problem is that an in-order traversal (Left -> Root -> Right) visits the nodes in ascending sorted order.

# If we had a sorted array of numbers, the minimum difference would always be between two adjacent elements. For example, in [1, 5, 8, 12], the minimum difference will be min(5-1, 8-5, 12-8), which is 3. The difference between non-adjacent elements like 8-1 will always be greater than the differences of the elements between them.

# We can apply this same logic directly to the BST without first storing all values in an array.

# The Algorithm: In-Order Traversal
# We can perform an in-order traversal. While traversing, we only need to keep track of the value of the previously visited node. For each new node we visit, we calculate the difference between its value and the previous node's value. We keep a running minimum of these differences.

# Initialize a variable min_difference to infinity.
# Initialize a variable previous_value to None.
# Define a function to perform an in-order traversal (traverse(node)).
# Inside the traversal function:
# First, recurse on the left child: traverse(node.left).
# When that returns, we are at the current node. Calculate the difference between node.val and previous_value. Update min_difference if this new difference is smaller.
# Update previous_value to the current node's value.
# Finally, recurse on the right child: traverse(node.right).
# Start the process by calling the traversal on the root.
# Return min_difference.
