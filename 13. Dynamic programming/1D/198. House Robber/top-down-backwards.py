class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        cache = {
            0: nums[0],
            1: max(nums[0], nums[1])
        }
        def solve(k):
            if k in cache:
                return cache[k]

            res = max(nums[k] + solve(k-2), solve(k-1))
            cache[k] = res
            return res


        return solve(n-1)

