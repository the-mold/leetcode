class Solution:
    def _any_point_is_within_area(self, points, idx1, idx2, A, B):
        for idx3, point3 in enumerate(points):
            if idx3 == idx1 or idx3 == idx2:
                continue
            C = points[idx3]
            
            # Check if point C is inside or on the border of the rectangle
            # formed by A (upper-left) and B (lower-right).
            if A[0] <= C[0] <= B[0] and A[1] >= C[1] >= B[1]:
                return True

        return False
    

    def numberOfPairs(self, points: List[List[int]]) -> int:
        count = 0
        for idx1, point1 in enumerate(points):
            for idx2, point2 in enumerate(points):
                if idx1 == idx2:
                    continue

                A = points[idx1]
                B = points[idx2]

                # Condition: A is on the upper left side of B.
                # This means A.x <= B.x and A.y >= B.y.
                # Also, they cannot be the same point.
                is_upper_left = A[0] <= B[0] and A[1] >= B[1]
                if not is_upper_left:
                    continue

                # cannot be the same point
                if A[0] == B[0] and A[1] == B[1]:
                    continue
                
                # check if there is no other point in the way
                if self._any_point_is_within_area(points, idx1, idx2, A, B):
                    continue

                count += 1
        
        return count

#T:O(n**3)
#S:O(1)