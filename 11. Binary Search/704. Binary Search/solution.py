class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Performs binary search to find the target in a sorted array.

        Args:
            nums: A list of integers sorted in ascending order.
            target: The integer to search for.

        Returns:
            The index of the target if it exists, otherwise -1.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            # Calculate the middle index. 
            # Using mid = left + (right - left) // 2 prevents potential overflow
            # in other languages, and is a good habit in Python as well.
            mid = left + (right - left) // 2

            # Check if the middle element is the target
            if nums[mid] == target:
                return mid
            
            # If the target is greater, it must be in the right half
            elif nums[mid] < target:
                left = mid + 1
            
            # If the target is smaller, it must be in the left half
            else:
                right = mid - 1

        # If the loop completes without finding the target
        return -1

# --- Complexity Analysis ---
# Time Complexity: O(log n)
# With each comparison, we eliminate half of the remaining search space.

# Space Complexity: O(1)
# We only use a few variables (left, right, mid) to store pointers, 
# so the space usage is constant regardless of the input size.

