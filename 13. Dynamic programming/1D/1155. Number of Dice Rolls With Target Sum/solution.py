class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}

        res_transform = 10**9 + 7

        def helper(dice_left, curr_target):
            if dice_left == 0:
                return 1 if curr_target == 0 else 0
            if curr_target < 0:
                return 0

            if (dice_left, curr_target) in memo:
                return memo[(dice_left, curr_target)]

            counts = 0
            for points in range(1, k+1):
                counts += helper(dice_left - 1, curr_target - points)
            
            counts = counts % res_transform

            memo[(dice_left, curr_target)] = counts
            return counts
        
        return helper(n, target)
      
# Complexity
# Time: O(n · target · k)
# Space: O(n · target) for memo, recursion depth O(n)
