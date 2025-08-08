import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        is_majority = math.floor(n / 2)
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
            
            if d[num] > is_majority:
                return num

# T: O(n)
# S: O(n)