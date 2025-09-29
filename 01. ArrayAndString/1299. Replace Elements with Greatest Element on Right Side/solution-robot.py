from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Replaces each element in an array with the greatest element to its right.
        The last element is replaced with -1.

        This is solved by iterating from right to left, keeping track of the
        maximum value encountered so far. This approach has a time complexity
        of O(n) and a space complexity of O(1) (if we modify the array in-place).
        """
        
        # Initialize right_max to -1, which will be the value for the last element.
        right_max = -1
        
        # Iterate through the array from right to left.
        # The range goes from the last index (len(arr) - 1) down to 0.
        for i in range(len(arr) - 1, -1, -1):
            # The new value for the current element `arr[i]` is the current
            # `right_max` we've seen so far from the right side.
            # We also need to store the original value of `arr[i]` in a 
            # temporary variable `new_max` before overwriting it.
            new_max = max(right_max, arr[i])
            
            # Replace the current element with the greatest element to its right.
            arr[i] = right_max
            
            # Update right_max to be the maximum of its current value and the
            # original value of the element we just processed.
            right_max = new_max
            
        return arr

# Example Usage:
solver = Solution()

# Example 1
arr1 = [17, 18, 5, 4, 6, 1]
output1 = solver.replaceElements(list(arr1)) # Pass a copy to not modify original
print(f"Input: {arr1}")
print(f"Output: {output1}") # Expected: [18, 6, 6, 6, 1, -1]
print("-" * 20)

# Example 2
arr2 = [400]
output2 = solver.replaceElements(list(arr2))
print(f"Input: {arr2}")
print(f"Output: {output2}") # Expected: [-1]