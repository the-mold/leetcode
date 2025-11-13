class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 0:
            return 0

        max_average = float("-inf")
        l = 0
        curr_sum = 0

        for r in range(len(nums)):
            curr_sum += nums[r]

            if r >= k - 1:
                max_average = max(max_average, curr_sum / k)

                curr_sum -= nums[l]
                l += 1
        
        return max_average

# T:O(n)
# S:O(1)
