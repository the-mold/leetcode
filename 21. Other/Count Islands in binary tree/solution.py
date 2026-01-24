class Solution:
  def solve(self, root ): #[1, 1, 0, 1, 1, null, 0]
    if not root:
      return 0
    
    parents = []
    self.solve(root, parents, None)
    return len(parents)
  
  def _solve(self, node, parents, last_node_value):
    if not node:
      return
    
    if last_node_value is None or last_node_value != node.val:
      parents.append(node)
    
    self._solve(node.left, parents, node.val)
    self._solve(node.right, parents, node.val)
    
    return

# T:O(n)
# S:O(n)