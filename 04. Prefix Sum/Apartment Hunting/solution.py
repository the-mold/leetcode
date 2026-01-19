def apartmentHunting(blocks, reqs):
    """
    Finds the optimal block to live in by minimizing the maximum distance 
    to any required building.
    This solution has an optimal time and space complexity.
    Args:
      blocks: A list of dictionaries, where each dictionary represents a block
              and its available facilities.
      reqs: A list of strings representing the required facilities.
    Returns:
      The index of the optimal block.
    """
    # Create a matrix to store the minimum distance from each block to each requirement.
    # Initialize distances to infinity to handle cases where a req is far away.
    min_dists_from_blocks = [[float('inf') for _ in reqs] for _ in blocks]
    # --- Pass 1: Calculate distances from left to right ---
    for i in range(len(blocks)):
        for j, req in enumerate(reqs):
            if blocks[i][req] == True:
                min_dists_from_blocks[i][j] = 0
            elif i > 0:
                min_dists_from_blocks[i][j] = min_dists_from_blocks[i - 1][j] + 1  # distance from the previous block + 1
                
    # --- Pass 2: Update with distances from right to left ---
    # Iterate backwards from the second-to-last block.
    for i in range(len(blocks) - 2, -1, -1):
        for j, req in enumerate(reqs):
            # The true minimum distance is the smaller of what we've already calculated
            # (distance to the left) and the distance to the right.
            min_dists_from_blocks[i][j] = min(
                min_dists_from_blocks[i][j], 
                min_dists_from_blocks[i + 1][j] + 1
            )
    # --- Pass 3: Find the block with the smallest maximum distance ---
    optimal_block_idx = -1
    min_farthest_dist = float('inf')
    for i in range(len(blocks)):
        # For each block, find the farthest you'd have to travel for any requirement.
        farthest_dist_at_block = max(min_dists_from_blocks[i])
        
        # If this block's farthest distance is better than the best we've seen,
        # it becomes the new optimal block.
        if farthest_dist_at_block < min_farthest_dist:
            min_farthest_dist = farthest_dist_at_block
            optimal_block_idx = i
            
    return optimal_block_idx
  
# Sample Input:
blocks = [
    {"gym": False, "school": True, "store": False},
    {"gym": True, "school": False, "store": False},
    {"gym": True, "school": True, "store": False},
    {"gym": False, "school": True, "store": False},
    {"gym": False, "school": True, "store": True},
]
reqs = ["gym", "school", "store"]
best_block_index = apartmentHunting(blocks, reqs)
print(f"The optimal block to live in is at index: {best_block_index}")

# Time Complexity: O(b * r)
# S: O(b * r)

# Explanation:

# The most efficient way to solve this problem is to pre-calculate the minimum distance from every block to every required building. 
# A brute-force approach would be too slow (O(b² * r)). The optimal solution uses dynamic programming across two passes.

# 1. First Pass (Left to Right): We iterate through the blocks from left to right. For each block, we calculate the distance to the nearest 
# required building to its left. If a building is at the current block, the distance is 0. Otherwise, it's 1 + the distance from the 
# previous block.

# 2. Second Pass (Right to Left): We then iterate from right to left. This time, we update our distances by considering the nearest required 
# building to the right. The true minimum distance for any block is the smaller of the distance calculated in the left-to-right pass and 
# the distance calculated in this right-to-left pass.

# 3. Find the Optimal Block: After the two passes, we have a complete data structure containing the shortest distance from every block 
# to every requirement. We can then iterate through this data one last time. For each block, we find the maximum distance we'd have to 
# travel to satisfy all requirements. The block with the smallest of these "maximum distances" is our answer.
