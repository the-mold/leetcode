from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotates an array to the right by k steps in-place using cyclic replacements.
        """
        n = len(nums)
        
        # If k is greater than n, rotating k times is the same as rotating k % n times.
        # For example, rotating a 7-element array 8 times is the same as rotating it once.
        k %= n

        # If k is 0, no rotation is needed.
        if k == 0:
            return

        # 'count' tracks the total number of elements placed in their correct positions.
        # The process is complete when all 'n' elements have been moved.
        count = 0
        
        # 'start' is the starting index for each cycle of replacements.
        start = 0
        
        # Continue until all elements have been moved.
        while count < n:
            # For each cycle, 'current' is the index of the element we are currently moving.
            # 'prev_val' holds the value of the element at the 'current' index.
            current = start
            prev_val = nums[start]

            # This inner loop performs one complete cycle of swaps.
            while True:
                # Calculate the next index where the 'prev_val' should be placed.
                next_idx = (current + k) % n
                
                # Swap the values:
                # - The value at 'next_idx' is temporarily stored in 'temp'.
                # - 'prev_val' is placed at 'next_idx'.
                # - 'temp' becomes the new 'prev_val' to be placed in the next iteration.
                temp = nums[next_idx]
                nums[next_idx] = prev_val
                prev_val = temp
                
                # Move to the next position in the cycle.
                current = next_idx
                
                # Increment the count of placed elements.
                count += 1

                # A cycle is complete when we return to the starting index.
                if start == current:
                    break
            
            # Move to the next starting index to begin a new cycle if needed.
            # This handles cases with multiple disjoint cycles.
            start += 1