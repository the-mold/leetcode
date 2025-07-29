class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n) for _ in range(m)]

        # all first row is 1 because there is only one way to come there
        for row in range(m):
            dp[row][0] = 1
        
        # all first col is 1 because there is only one way to come there
        for col in range(n):
            dp[0][col] = 1

        for row in range(1, m):
            for col in range(1, n):
                # add cells on the left and on the top. These two cells are the only possibility to come to the currentcell
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        print("dp", dp)
        return dp[m - 1][n - 1]

# Time Complexity: O(m×n) - We fill in each cell of the m×n grid 
# Space Complexity: O(m×n) - We store the entire grid