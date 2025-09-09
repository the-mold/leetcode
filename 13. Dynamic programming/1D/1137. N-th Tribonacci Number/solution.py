class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        # state - tribonacci number at given index

        # 1. datastructure
        dp = [0] * (n + 1)

        # 2. relation
        #dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

        #3. base case
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

        return dp[n]
    
# Time Complexity: O(n)
# The time complexity is determined by the dominant operation in the function, which is the for loop.

# Initialization: The if checks and the creation of the dp array (dp = [0] * (n + 1)) take time proportional to n in the worst case (for the array creation).
# Loop: The for loop runs from 3 to n. This means it will execute n - 2 times.
# Inside the Loop: Each iteration of the loop involves a fixed number of operations: three array lookups and two additions. These are constant time, O(1), operations.
# Since the loop runs approximately n times, and the work inside the loop is constant, the overall time complexity is O(n). The runtime grows linearly with the input n.

# Space Complexity: O(n)
# The space complexity is determined by the amount of extra memory the algorithm uses, which is primarily the dp array.

# DP Array: The algorithm allocates an array named dp with n + 1 elements to store the Tribonacci numbers.
# Memory Usage: The memory required for this array grows directly in proportion to the input n.