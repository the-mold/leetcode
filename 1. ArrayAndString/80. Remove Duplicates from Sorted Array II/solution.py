import math 

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        idx = 0

        checked_int = math.inf
        current_int_occurences = 0
        for num in nums:
            
            if num != checked_int:
                checked_int = num
                current_int_occurences = 0
            
            if current_int_occurences < 2:
                nums[idx] = num
                current_int_occurences += 1
                idx += 1
        
        return idx