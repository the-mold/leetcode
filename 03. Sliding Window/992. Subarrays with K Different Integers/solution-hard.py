from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
        Count subarrays with exactly k distinct integers using a single-pass approach.
        
        Key idea: For each right pointer position, find the minimum left position
        where we have exactly k distinct elements, then count all valid subarrays
        ending at right.
        """
        # Frequency map to track count of each element in current window
        freq = [0] * (len(nums) + 1)
        
        total_subarrays = 0
        left = 0  # Left boundary of the window
        right = 0  # Right boundary of the window
        distinct_remaining = k  # How many more distinct elements we need
        extra_subarrays = 0  # Number of extra valid starting positions
        
        while right < len(nums):
            current_num = nums[right]
            
            # Add current element to the window
            freq[current_num] += 1
            
            # If this is a new distinct element, we need one less distinct element
            if freq[current_num] == 1:
                distinct_remaining -= 1
            
            # If we have too many distinct elements (more than k)
            if distinct_remaining < 0:
                # Shrink window from left until we have exactly k distinct elements
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    distinct_remaining += 1  # We removed a distinct element
                left += 1
                extra_subarrays = 0  # Reset extra count when we shrink
            
            # If we have exactly k distinct elements
            if distinct_remaining == 0:
                # Shrink from left as much as possible while maintaining k distinct elements
                # This finds all valid starting positions for subarrays ending at right
                while freq[nums[left]] > 1:
                    freq[nums[left]] -= 1
                    left += 1
                    extra_subarrays += 1
                
                # Count all valid subarrays ending at position right:
                # - The subarray starting at current left position: 1
                # - All subarrays from the extra positions we found: extra_subarrays
                total_subarrays += (extra_subarrays + 1)
            
            right += 1
        
        return total_subarrays


# Test cases
solution = Solution()
print(solution.subarraysWithKDistinct([1,2,1,2,3], 2))  # Output: 7
print(solution.subarraysWithKDistinct([1,2,1,3,4], 3))  # Output: 3