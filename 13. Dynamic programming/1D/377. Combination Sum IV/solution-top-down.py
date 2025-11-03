class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def helper(curr_target):
            if curr_target == 0:
                return 1
            if curr_target < 0:
                return 0
            if curr_target in memo:
                return memo[curr_target]
            
            count = 0
            for num in nums:
                count += helper(curr_target - num)
            
            memo[target] = count
            return count

        return helper(target)