# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def leaf_layers(root):
  layers = []
  _leaf_layers(root, layers)
  return leaves

def _leaf_layers(node, layers):
  if not node:
    return -1

  left = _leaf_layers(node.left, layers)
  right = _leaf_layers(node.right, layers)
  height = 1 + max(left, right)

  if len(layers) == height:
    layers.append([])
  
  layers[height].append(node.val)
  
  return height

# T:O(n)
# S:O(n)
