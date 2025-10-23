# The idea of Kadane's algorithm is to traverse over the array from left to right and for each element, find the maximum sum among all subarrays ending at that element. The result will be the maximum of all these values. 
# To calculate the maximum sum of subarray ending at current element, say maxEnding, we can use the maximum sum ending at the previous element.
# So for any element, we have two choices:
# Choice 1: Extend the maximum sum subarray ending at the previous element by adding the current element to it. If the maximum subarray sum ending at the previous index is positive, then it is always better to extend the subarray.
# Choice 2: Start a new subarray starting from the current element. If the maximum subarray sum ending at the previous index is negative, it is always better to start a new subarray from the current element.
# This means that maxEnding at index i = max(maxEnding at index (i - 1) + arr[i], arr[i]) and the maximum value of maxEnding at any index will be our answer.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Stores the result (maximum sum found so far)
        res = nums[0]
        # Maximum sum of subarray ending at current position
        maxEnding = nums[0]

        for i in range(1, len(nums)):
            # Either extend the previous subarray or start 
            # new from current element
            maxEnding = max(maxEnding + nums[i], nums[i])
            
            # Update result if the new subarray sum is larger
            res = max(res, maxEnding)

        return res


#T:O(n)
#S:O(1)