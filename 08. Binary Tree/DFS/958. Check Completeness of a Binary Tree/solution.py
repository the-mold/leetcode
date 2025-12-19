# Intuition: go through the tree level-by-level with BFS.
# Once you get a None node, all nodes after it MUST be None. Only this would be a complete tree.
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque()
        q.append(root)

        seen_none = False
        while q:
            node = q.popleft()

            if node and seen_none:
                return False

            if not node:
                seen_none = True
                continue

            q.append(node.left)
            q.append(node.right)
    
        return True
      
# T:O(n)
#S:O(n)