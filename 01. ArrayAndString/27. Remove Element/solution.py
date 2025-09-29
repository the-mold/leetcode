from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Removes all occurrences of val in nums in-place.

        Args:
            nums: A list of integers.
            val: The integer value to remove.

        Returns:
            The number of elements in nums which are not equal to val.
        """
        k = 0  # Pointer for the next position to place an element not equal to val
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

# T: O(n)
# S: O(1)
