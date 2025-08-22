"""
DFS Templates for Binary Trees
Master these templates and you'll be able to solve most DFS tree problems!
"""

from binary_tree_node import TreeNode, create_sample_tree


# ============================================================================
# TEMPLATE 1: Basic Recursive DFS (Most Important!)
# ============================================================================

def dfs_recursive_template(root):
    """
    THE MOST IMPORTANT TEMPLATE TO MEMORIZE!
    This is your go-to pattern for 80% of tree problems.
    
    Steps:
    1. Handle base case (null node)
    2. Process current node (if needed)
    3. Recursively process left subtree
    4. Recursively process right subtree
    5. Return result (if needed)
    """
    # Step 1: Base case
    if not root:
        return None  # or 0, [], False, etc. depending on problem
    
    # Step 2: Process current node (optional, depends on problem)
    # Do something with root.val
    
    # Step 3 & 4: Recursive calls
    left_result = dfs_recursive_template(root.left)
    right_result = dfs_recursive_template(root.right)
    
    # Step 5: Combine results and return (optional)
    # return some_combination(root.val, left_result, right_result)
    return None


# ============================================================================
# TEMPLATE 2: DFS with Helper Function (When you need extra parameters)
# ============================================================================

def dfs_with_helper_template(root):
    """
    Use this when you need to pass additional parameters down the recursion
    or maintain state across recursive calls.
    """
    def helper(node, param1, param2):
        # Base case
        if not node:
            return None
        
        # Process current node
        # Use param1, param2 as needed
        
        # Recursive calls with updated parameters
        left_result = helper(node.left, updated_param1, updated_param2)
        right_result = helper(node.right, updated_param1, updated_param2)
        
        # Combine and return
        return None
    
    # Start the recursion with initial parameters
    return helper(root, initial_param1, initial_param2)


# ============================================================================
# TEMPLATE 3: DFS with Global/Nonlocal Variables
# ============================================================================

def dfs_with_global_state_template(root):
    """
    Use this when you need to maintain state that persists across all recursive calls.
    Common for problems like "count nodes", "find maximum", etc.
    """
    result = []  # or any other data structure
    
    def dfs(node):
        nonlocal result  # or use self.result in a class
        
        if not node:
            return
        
        # Process current node and update global state
        result.append(node.val)  # or update result somehow
        
        # Recursive calls
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return result



# ============================================================================
# TEMPLATE 5: DFS with Return Value Combination
# ============================================================================

def dfs_return_combination_template(root):
    """
    Use this when you need to combine results from left and right subtrees.
    Common for problems like tree height, tree diameter, etc.
    """
    def dfs(node):
        if not node:
            return 0  # or appropriate base value
        
        # Get results from subtrees
        left_result = dfs(node.left)
        right_result = dfs(node.right)
        
        # Combine results based on problem requirements
        current_result = 1 + max(left_result, right_result)  # example: height
        
        return current_result
    
    return dfs(root)


# ============================================================================
# EXAMPLES: Applying the Templates
# ============================================================================

def count_nodes(root):
    """Example: Count total nodes in tree"""
    if not root:
        return 0
    
    left_count = count_nodes(root.left)
    right_count = count_nodes(root.right)
    
    return 1 + left_count + right_count


def tree_height(root):
    """Example: Find height of tree"""
    if not root:
        return 0
    
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    
    return 1 + max(left_height, right_height)


def find_target(root, target):
    """Example: Find if target exists in tree"""
    if not root:
        return False
    
    if root.val == target:
        return True
    
    return find_target(root.left, target) or find_target(root.right, target)


