class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0

        n = len(height)
        for i in range(1, n - 1):
            left_max = 0
            right_max = 0

            for l in range(i, -1, -1):
                left_max = max(left_max, height[l])
            
            for r in range(i, n):
                right_max = max(right_max, height[r])

            water =  min(left_max, right_max) - height[i]
            if water > 0:
                ans += water
        
        return ans
    
#T:O(n^2)
#S:O(1)

#Intuition
# For every point(except of the first and last becaused it makes no sense), calculate the maximum height on the left and on the right.
# Formula for water for any given point `i` is: min(left_max, right_max) - height[i].
