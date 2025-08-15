class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height)

        left_max_arr, right_max_arr = [0] * n, [0] * n

        # left side

        # assign first height element as firs left max element. It is known and will not change
        left_max_arr[0] = height[0]
        # pre-calculate all left maximums for every point
        for i in range(1, n):
            left_max_arr[i] = max(left_max_arr[i-1], height[i])

        # Right side

        # assign last height element as last right max element. It is known and will not change
        right_max_arr[n-1] = height[n-1]
        # pre-calculate all right maximums for every point
        for i in range(n-2,-1,-1):
            right_max_arr[i] = max(right_max_arr[i+1], height[i])

        for i in range(n):
            ans += min(left_max_arr[i], right_max_arr[i]) - height[i]

        return ans

#T:O(n)
#S:O(n)

#Note! To understand it, start with brute force solution. This dp solution only pre-computes left and right maximum for any given point.
# Otherwise the logic is the same as in brute force.