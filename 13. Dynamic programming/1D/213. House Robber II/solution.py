# Intuition: first and last houses are adjecent. They cannot be robbed in one go.
# Problem divides in two subproblems: 
# 1. houses from first to n-1
# 2. houses from second to n 

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
            
        memo1 = {}
        memo2 = {}

        def solve(i, houses, memo):
            if i >= len(houses):
                return 0
            if i in memo:
                return memo[i]
            
            rob_house = houses[i] + solve(i + 2, houses, memo)
            skip_house = solve(i + 1, houses, memo)

            res = max(rob_house, skip_house)

            memo[i] = res
            return res

        return max(
          # rob hoses starting from first to n-1
          solve(0, nums[:n-1], memo1), 
          # rob houses from second to n
          solve(0, nums[1:], memo2)
        )

# T:O(2n) => O(n)
# S:O(2n) => O(n)
