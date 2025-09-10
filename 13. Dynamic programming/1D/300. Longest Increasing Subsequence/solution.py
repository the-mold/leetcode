from types import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # state - logest increasing subsequence that ends at i

        # ds
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            # check all numbers that come before i
            for j in range(i):
                # if current number is bigger than the previous
                if nums[i] > nums[j]:
                    # set current dp element to maximum of current value OR value of previous logest subsequence + 1
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
