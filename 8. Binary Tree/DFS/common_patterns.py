"""
Common DFS Patterns for Binary Trees
Practice these until they become second nature!
"""

from binary_tree_node import TreeNode, create_sample_tree


# ============================================================================
# PREORDER TRAVERSAL (Root -> Left -> Right)
# ============================================================================

def preorder_recursive(root):
    """
    Preorder: Process root, then left subtree, then right subtree
    Use when: You need to process parent before children (e.g., copying tree)
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        
        result.append(node.val)  # Process root first
        dfs(node.left)           # Then left subtree
        dfs(node.right)          # Then right subtree
    
    dfs(root)
    return result


# ============================================================================
# INORDER TRAVERSAL (Left -> Root -> Right)
# ============================================================================

def inorder_recursive(root):
    """
    Inorder: Process left subtree, then root, then right subtree
    Use when: You need sorted order in BST, or symmetric processing
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        
        dfs(node.left)           # Left subtree first
        result.append(node.val)  # Then process root
        dfs(node.right)          # Then right subtree
    
    dfs(root)
    return result


# ============================================================================
# POSTORDER TRAVERSAL (Left -> Right -> Root)
# ============================================================================

def postorder_recursive(root):
    """
    Postorder: Process left subtree, then right subtree, then root
    Use when: You need to process children before parent (e.g., deleting tree)
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        
        dfs(node.left)           # Left subtree first
        dfs(node.right)          # Then right subtree
        result.append(node.val)  # Finally process root
    
    dfs(root)
    return result



# ============================================================================
# PATH-BASED PATTERNS
# ============================================================================

def find_all_paths_to_leaves(root):
    """
    Find all paths from root to leaves
    Common pattern for path-sum problems
    """
    if not root:
        return []
    
    all_paths = []
    
    def dfs(node, current_path):
        if not node:
            return
        
        # Add current node to path
        current_path.append(node.val)
        
        # If leaf node, save the path
        if not node.left and not node.right:
            all_paths.append(current_path[:])  # Make a copy
        else:
            # Continue exploring
            dfs(node.left, current_path)
            dfs(node.right, current_path)
        
        # Backtrack: remove current node from path
        current_path.pop()
    
    dfs(root, [])
    return all_paths


def path_sum_exists(root, target_sum):
    """
    Check if any root-to-leaf path sums to target
    Classic DFS with parameter passing
    """
    def dfs(node, remaining_sum):
        if not node:
            return False
        
        # Update remaining sum
        remaining_sum -= node.val
        
        # If leaf node, check if we've reached target
        if not node.left and not node.right:
            return remaining_sum == 0
        
        # Check either subtree
        return dfs(node.left, remaining_sum) or dfs(node.right, remaining_sum)
    
    return dfs(root, target_sum)


# ============================================================================
# LEVEL/DEPTH PATTERNS
# ============================================================================

def nodes_at_level(root, target_level):
    """
    Get all nodes at a specific level (0-indexed)
    """
    result = []
    
    def dfs(node, current_level):
        if not node:
            return
        
        if current_level == target_level:
            result.append(node.val)
            return  # No need to go deeper
        
        dfs(node.left, current_level + 1)
        dfs(node.right, current_level + 1)
    
    dfs(root, 0)
    return result



# ============================================================================
# VALIDATION PATTERNS
# ============================================================================

def is_valid_bst(root):
    """
    Validate if tree is a valid Binary Search Tree
    Pattern: DFS with bounds checking
    """
    def dfs(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (dfs(node.left, min_val, node.val) and 
                dfs(node.right, node.val, max_val))
    
    return dfs(root, float('-inf'), float('inf'))


# ============================================================================
# Trigger recursion starting from EVERY single node
# ============================================================================

def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    def countPathFromNode(node, currentSum):
        if not node:
            return 0
        
        currentSum += node.val
        paths_found = 1 if currentSum == targetSum else 0
        paths_found += countPathFromNode(node.left, currentSum)
        paths_found += countPathFromNode(node.right, currentSum)

        return paths_found

    if not root:
        return 0

    #count paths from current node
    pathsFromRoot = countPathFromNode(root, 0)

    # do the same for left and right children. This is how you trigger function for every node in the tree. First do smth for root, then for left and right start the main function again.
    pathsFromLeft = self.pathSum(root.left, targetSum)
    pathsFromRight = self.pathSum(root.right, targetSum)

    return pathsFromRoot + pathsFromLeft + pathsFromRight
