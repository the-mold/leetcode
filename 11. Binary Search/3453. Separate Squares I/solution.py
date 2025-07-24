class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # 1. calculate target area
        areas = [length * length for _, _, length in squares]
        total_area = sum(areas)
        target_area_above_line = total_area / 2.0

        # 2. Get low-high params
        all_low_points = [y for _, y, _ in squares]
        low = min(all_low_points)
        min_low = low

        all_high_points = [y + l for _, y, l in squares]
        high = max(all_high_points)
        max_high = high

        # 3. define helper function that calculates area above the line for each squar for some line
        def get_area_above_line(line_y):
            area = 0

            for x, y, l in squares:
                square_top = y + l
                square_bottm = y

                # Case 1: line is above the square, I need to return 0
                if line_y >= square_top:
                    area += 0
                # Case 2: line is below both squares, I need to return total area
                elif line_y <= square_bottm:
                    area += l * l
                # Case 3: line intersects i the square. Add area above the line 
                else:
                    area_above_line = l * (square_top - line_y)
                    area += area_above_line

            return area

        # 4. Do binary search
        for i in range(100):
            mid = (low + high) / 2.0
            area_above_line = get_area_above_line(mid)

            if area_above_line > target_area_above_line:
                low = mid       # assign just mid when working with floats 
            else:
                high = mid      # assign just mid when working with floats 
        
        return low #return low at the end of the binary search because it represents the minimum y-coordinate that satisfies our condition, which is exactly what the problem asks for.

# Time Complexity
# Overall Complexity: O(n log k)
# Where n is the number of squares
# k represents the range of possible y-coordinates divided by the required precision
# Breaking it down:
# Binary search: O(log k) iterations
# We perform 100 iterations, which is a constant, but theoretically it's O(log k)
# For each iteration, we calculate area above the line: O(n)
# We process each of the n squares once per iteration
# Combined: O(n) * O(log k) = O(n log k)
# Other operations:
# Calculating total area: O(n)
# Finding min/max y-coordinates: O(n)
# These are one-time operations and don't affect the asymptotic complexity


# Space Complexity
# The space complexity is O(1) - constant space:
# We only store a fixed number of variables regardless of input size
# No additional data structures that scale with input size
# Practical Performance
# While the theoretical complexity is O(n log k), in practice:

# The binary search iterations are fixed at 100
# This makes the practical time complexity closer to O(n)
# The algorithm will efficiently handle large numbers of squares