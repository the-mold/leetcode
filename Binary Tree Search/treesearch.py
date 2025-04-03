def transverse_tree(root):
  if root:
    transverse_tree(root.left)
    print(root.value)
    transverse_tree(root.right)

T: O(n)
S: O(n) 


# Example tree:
#         4
#        / \
#       2   6
#      / \  / \
#     1   3 5  7

# Will print out:
# 1 2 3 4 5 6 7
