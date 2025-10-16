class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort the balloons by their end coordinate (x_end).
        # This ensures we always handle the balloon that finishes earliest first.
        points.sort(key=lambda x: x[1])

        count = 0
        prev_end = None
        for start, end in points:
            if prev_end != None and prev_end >= start:
                continue
            
            count += 1
            prev_end = end
        
        return count

# T:O(nlogn)
# S:O(n) because of soring