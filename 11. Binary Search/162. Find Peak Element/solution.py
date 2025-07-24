class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        """
        Finds a peak element in the array using binary search.
        A peak element is strictly greater than its neighbors.
        The algorithm runs in O(log n) time.

        Args:
            nums: A list of integers.

        Returns:
            The index of any peak element.
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            
            # Compare the middle element with its right neighbor.
            if nums[mid] > nums[mid + 1]:
                # The peak is in the left half, including mid.
                # We are on a downward slope, so a peak must be to the left or at mid.
                right = mid
            else:
                # The peak is in the right half, excluding mid.
                # We are on an upward slope, so a peak must be to the right.
                left = mid + 1
        
        # When the loop ends, left == right, and we have found a peak.
        # This works because the search space is guaranteed to contain a peak.
        return left
  
  
# The Logic
# The key insight is that we don't need to find a specific value, but rather a position that satisfies a condition (being a peak). We can use binary search to systematically narrow down the search space where a peak must exist.

# Consider any element nums[mid] and its right neighbor nums[mid + 1]:

# If nums[mid] > nums[mid + 1]: This means we are on a "downward slope" to the right. A peak must exist either at mid itself or somewhere to its left. Why? Because we know the array eventually came from nums[-1] = -∞, so if we keep moving left from mid, we will either find a value that is smaller than nums[mid] (making mid a peak) or the values will keep increasing until they hit the start of the array (making the start a peak). Therefore, we can safely discard the entire right half of the search space.
# If nums[mid] < nums[mid + 1]: This means we are on an "upward slope". A peak must exist somewhere to the right of mid. Why? Because the value is increasing at mid + 1, but we know it must eventually "fall off" to meet nums[n] = -∞. This guarantees a peak lies in the right half. Therefore, we can safely discard mid and everything to its left.
# By repeatedly applying this logic, we will converge on a single index, which is guaranteed to be a peak.

# The Algorithm
# Initialize pointers left = 0 and right = len(nums) - 1.
# Loop as long as left < right. This ensures the search space has at least two elements to compare.
# Find the middle index mid.
# Compare nums[mid] with nums[mid + 1].
# If nums[mid] is greater, it means a peak is in the left half (including mid), so we set right = mid.
# Otherwise, the peak must be in the right half, so we set left = mid + 1.
# When the loop terminates, left and right will be equal, pointing to a peak element. Return left.