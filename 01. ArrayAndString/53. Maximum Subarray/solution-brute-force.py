class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]

        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                res = max(res, curr_sum)
        
        return res
      
# T:O(n**2)
# S:O(1)