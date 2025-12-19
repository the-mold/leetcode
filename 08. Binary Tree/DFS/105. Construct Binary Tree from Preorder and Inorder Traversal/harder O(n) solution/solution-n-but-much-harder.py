# Idea: precalculate all indexes in in_order_index in order not to do index loockups .index() in O(n).
# Also use just index pointers instead of slicing arrays.

def build_tree_in_pre(in_order, pre_order):
  in_order_index = {}
  for idx, v in enumerate(in_order):
    in_order_index[v] = idx
  
  return _build_tree_in_pre(in_order, pre_order, in_order_index, 0, len(in_order) - 1, 0, len(in_order) - 1)

def _build_tree_in_pre(in_order, pre_order, in_order_index, in_start, in_end, pre_start, pre_end):
  # base case when pointers cross. End cannot be less than start
  if in_start > in_end:
    return None

  parent_val = pre_order[pre_start]
  node = Node(parent_val)
  mid = in_order_index[parent_val]
  left_size = mid - in_start
  node.left = _build_tree_in_pre(
    in_order, 
    pre_order, 
    in_order_index,
    in_start, 
    mid - 1, 
    pre_start+1, 
    pre_start + left_size
  )

  node.right = _build_tree_in_pre(
    in_order, 
    pre_order, 
    in_order_index,
    mid + 1, 
    in_end, 
    pre_start + left_size + 1, 
    pre_end
  )

  return node

# T:O(n)
# S:O(n)
