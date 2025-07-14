def maxDepth(root):
    if not root:
        return 0
    
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

#T:O(n)
#S:O(n)   <---- number of recursions