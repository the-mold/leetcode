class Solution:
    def arrangeCoins(self, n: int) -> int:
        row = 1

        while n >= row:
            n -= row
            row += 1
        
        return row - 1

# The time complexity of arrangeCoins_iterative(n) is O(√n).

# Analysis:

# The while loop continues as long as n >= row, where:

# We subtract row from n in each iteration
# row starts at 1 and increments by 1 each time
# Key insight: The loop runs for k iterations where k is the number of complete rows. Since we need k(k+1)/2 ≤ n coins total, we can solve for k:

# k(k+1)/2 ≈ k²/2 ≤ n
# k² ≤ 2n
# k ≤ √(2n)
# Therefore, the loop runs approximately √(2n) times, which simplifies to O(√n).

# Space complexity: O(1) - only using a few variables regardless of input size.

# This is why the mathematical solution arrangeCoins(n) with O(1) complexity is more efficient than the iterative approach, especially for large values of n.