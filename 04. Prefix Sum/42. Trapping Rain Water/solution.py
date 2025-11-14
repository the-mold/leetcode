class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        right = [0] * n
        left = [0] * n

        # left side

        # assign first height element as first left max element. It is known and will not change
        max_left = 0
        for i in range(n):
            max_left = max(max_left, height[i])
            left[i] = max_left

        # Right side

        # assign last height element as last right max element. It is known and will not change
        max_right = 0
        for i in range(n-1, -1, -1):
            max_right = max(max_right, height[i])
            right[i] = max_right

        ans = 0
        for i in range(1, n-1):
            max_left_at_point = left[i]
            max_right_at_point = right[i]
            ans += min(max_left_at_point, max_right_at_point) - height[i]

        return ans


#T:O(n)
#S:O(n)

#Note! To understand it, start with brute force solution. This solution only pre-computes left and right maximum for any given point.
# Otherwise the logic is the same as in brute force.