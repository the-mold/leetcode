class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def solve(i):
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            rob_house = nums[i] + solve(i+2)
            skip_house = solve(i+1)
            res = max(rob_house, skip_house)

            memo[i] = res
            return res

        return solve(0)
# T:O(n), Note! without memo it woulf be 2**N. For every n the amount of work doubles(2). It grows exponentially.
# S:O(n)
