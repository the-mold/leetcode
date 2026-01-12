class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self._findTargetSumWays(nums, target, 0, 0, {})

    def _findTargetSumWays(self, nums, target, idx, curr_sum, memo):
        key = (idx, curr_sum)
        if key in memo:
            return memo[key]

        if idx == len(nums) and target == curr_sum:
            return 1
        if idx == len(nums):
            return 0

        add = self._findTargetSumWays(nums, target, idx + 1, curr_sum + nums[idx], memo)
        sub = self._findTargetSumWays(nums, target, idx + 1, curr_sum - nums[idx], memo)

        memo[key] = add + sub
        return memo[key]
      
#T:O(n*m)
#S:O(n*m)