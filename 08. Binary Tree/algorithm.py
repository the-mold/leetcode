# DFS
#Recursive solution(usually best for path finding):
def depth_first_values(root):
  if not root:
    return []

  left = depth_first_values(root.left)
  right = depth_first_values(root.right)
  return [root.val] + left + right

#Stack solution:
def depth_first_values(root):
  if not root:
    return []
  
  values = []
  stack = [root]
  
  while stack:
    current = stack.pop()
    values.append(current.val)

    if current.right:
      stack.append(current.right)
    
    if current.left:
      stack.append(current.left)

  return values


# BFS
import collections
def breadth_first_values(root):
  if not root:
    return []
  
  values = []
  queue = collections.deque([root])
  
  while queue:
    current = queue.popleft()
    values.append(current.val)

    if current.right:
      queue.append(current.right)
    
    if current.left:
      queue.append(current.left)

  return values