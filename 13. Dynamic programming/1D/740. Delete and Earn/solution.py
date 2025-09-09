class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = {}
        max_number = 0

        for num in nums:
            points[num] = points.get(num, 0) + num
            max_number = max(max_number, num)

        # state - max number of points i get in certain index

        # 1. dp, where dp[num] will store the maximum amount of points we can gain if we only considered numbers from 0 to num (inclusive)
        dp = [0] * (max_number + 1)

        #2. relation
        #dp[i] = max(dp[i - 1], dp[i - 2] + dp[i])

        #3. base case
        dp[0] = 0
        dp[1] = points.get(1, 0) #the total points we can earn by taking all occurrences of the number 1

        for i in range(2, max_number + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + points.get(i, 0))

        return dp[max_number]
