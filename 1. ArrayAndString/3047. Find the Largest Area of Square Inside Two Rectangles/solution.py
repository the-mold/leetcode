class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        """
        Find the maximum area of a square that can fit inside the intersecting region of at least two rectangles.

        Args:
            bottomLeft: List[List[int]] - Bottom-left coordinates of each rectangle [a_i, b_i]
            topRight: List[List[int]] - Top-right coordinates of each rectangle [c_i, d_i]
            
        Returns:
            int - Maximum area of a square that can fit inside the intersecting region of at least two rectangles,
                or 0 if no such square exists
        """
        n = len(bottomLeft)
        max_square_area = 0

        # Check all pairs of rectangles
        for i in range(n):
            for j in range(i + 1, n):
                # Find the intersection of rectangles i and j
                # Intersection bottom-left: max of the two bottom-lefts
                int_bl_x = max(bottomLeft[i][0], bottomLeft[j][0])
                int_bl_y = max(bottomLeft[i][1], bottomLeft[j][1])
                
                # Intersection top-right: min of the two top-rights
                int_tr_x = min(topRight[i][0], topRight[j][0])
                int_tr_y = min(topRight[i][1], topRight[j][1])
                
                # Check if there is a valid intersection
                if int_bl_x < int_tr_x and int_bl_y < int_tr_y:
                    # Calculate the side length of the largest square that can fit
                    side_length = min(int_tr_x - int_bl_x, int_tr_y - int_bl_y)
                    max_square_area = max(max_square_area, side_length * side_length)

        return max_square_area

# Time Complexity: O(n²) where n is the number of rectangles. We check all pairs of rectangles.
# Space Complexity: O(1) as we only use a constant amount of extra space.
