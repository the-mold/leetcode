from typing import List

def islandPerimeter(grid: List[List[int]]) -> int:
    """
    Calculates the perimeter of a single island in a grid.

    Args:
        grid: A list of lists of integers, where 1 is land and 0 is water.

    Returns:
        The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # This is a land cell
                # Check UP
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                
                # Check DOWN
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                
                # Check LEFT
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                
                # Check RIGHT
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1
    
    return perimeter



# Method: Count Edges by Checking Neighbors
# This is the most direct approach. We can iterate through every cell in the grid. For each land cell (1), we check its four neighbors (up, down, left, right). If a neighbor is water (0) or is outside the grid boundary, that shared edge is part of the perimeter.

# Initialize perimeter = 0.
# Loop through each cell (r, c) of the grid.
# If grid[r][c] is a land cell:
# Check the cell above (r-1, c). If it's water or out of bounds, add 1 to perimeter.
# Check the cell below (r+1, c). If it's water or out of bounds, add 1 to perimeter.
# Check the cell to the left (r, c-1). If it's water or out of bounds, add 1 to perimeter.
# Check the cell to the right (r, c+1). If it's water or out of bounds, add 1 to perimeter.
# Return the total perimeter.


# Complexity
# Time Complexity: O(R * C)
# The time complexity is O(R * C), which is linear in the total number of cells in the grid.

# The algorithm consists of a nested loop that iterates through every single cell of the grid exactly once.
# The outer loop runs R times (for each row).
# The inner loop runs C times (for each column).
# Inside the loop, the operations performed (checking the value of the current cell and its four neighbors) are all constant time, O(1).
# Since every cell is visited and a constant amount of work is done for each, the total time taken is directly proportional to the number of cells, R * C.

# Space Complexity: O(1)
# The space complexity is O(1), which means it uses a constant amount of extra space.

# The algorithm uses only a few variables to store simple values: rows, cols, and perimeter.
# The amount of memory required for these variables does not change regardless of the size of the input grid.
# It does not use any auxiliary data structures (like a separate "visited" grid, a stack, or a queue) that would grow in size with the input grid. The calculation is done in place by just reading the grid values.
# In summary, the solution is quite efficient, with linear time complexity and constant space complexity.