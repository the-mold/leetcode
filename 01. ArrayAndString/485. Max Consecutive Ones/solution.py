from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current_count = 0

        for i, val in enumerate(nums):
            if val == 1:
                current_count += 1
            else:
                max_count = max(max_count, current_count)
                current_count = 0
        
        # read result of the last loop
        max_count = max(max_count, current_count)

        return max_count

# T:O(n)
# S:O(1)
