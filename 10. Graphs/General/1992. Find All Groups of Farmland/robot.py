from typing import List

def findFarmland(land: List[List[int]]) -> List[List[int]]:
    """
    Finds the coordinates of all rectangular farmland groups in a grid.

    Args:
        land: A 0-indexed m x n binary matrix where 1 is farmland and 0 is forest.

    Returns:
        A list of 4-element lists [r1, c1, r2, c2] representing the 
        top-left and bottom-right coordinates of each farmland group.
    """
    if not land or not land[0]:
        return []

    rows, cols = len(land), len(land[0])
    farmland_groups = []

    for r in range(rows):
        for c in range(cols):
            if land[r][c] == 1:
                # This is the top-left corner of a new group
                r1, c1 = r, c
                
                # Find the bottom-right corner of the rectangle
                r2, c2 = r1, c1
                while r2 + 1 < rows and land[r2 + 1][c1] == 1:
                    r2 += 1
                while c2 + 1 < cols and land[r1][c2 + 1] == 1:
                    c2 += 1
                
                # Add the found group to our results
                farmland_groups.append([r1, c1, r2, c2])
                
                # Mark this group as visited by changing 1s to 0s
                for i in range(r1, r2 + 1):
                    for j in range(c1, c2 + 1):
                        land[i][j] = 0
    
    return farmland_groups