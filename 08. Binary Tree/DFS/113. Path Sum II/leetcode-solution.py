# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x: int) -> None:
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def recurseTree(
        self,
        node: TreeNode,
        remainingSum: int,
        pathNodes: List[int],
        pathsList: List[List[int]],
    ) -> None:

        if not node:
            return

        # Add the current node to the path's list
        pathNodes.append(node.val)

        # Check if the current node is a leaf and also, if it
        # equals our remaining sum. If it does, we add the path to
        # our list of paths
        if remainingSum == node.val and not node.left and not node.right:
            pathsList.append(list(pathNodes))
        else:
            # Else, we will recurse on the left and the right children
            self.recurseTree(
                node.left, remainingSum - node.val, pathNodes, pathsList
            )
            self.recurseTree(
                node.right, remainingSum - node.val, pathNodes, pathsList
            )

        # We need to pop the node once we are done processing ALL of it's
        # subtrees.
        pathNodes.pop()

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        pathsList = []
        self.recurseTree(root, sum, [], pathsList)
        return pathsList

# Complexity Analysis

# Time Complexity: O(N**2) where N are the number of nodes in a tree. In the worst case, we could have a complete binary tree and if that is the case, then there would be N/2 leafs. For every leaf, we perform a potential O(N) operation of copying over the pathNodes nodes to a new list to be added to the final pathsList. Hence, the complexity in the worst case could be O(N**2).

# Space Complexity: O(N). The space complexity, like many other problems is debatable here. I personally choose not to consider the space occupied by the output in the space complexity. So, all the new lists that we create for the paths are actually a part of the output and hence, don't count towards the final space complexity. The only additional space that we use is the pathNodes list to keep track of nodes along a branch.
    