class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n != 0:
            ans += 1
            # this is a trick to remove the right most 1 from bit number. See example below.
            n = n & (n-1)
        
        return ans

#T:O(nuberOfOnesInBitRepresentation)
#S:O(1)

# Intuition
# The operation with n & (n-1) is a bit manipulation trick to remove right most 1 from bit representation of n.
# The & operation returns 1 only when both bits are 1:
# 0 & 0 -> 0
# 0 & 1 -> 0
# 1 & 0 -> 0
# 1 & 1 -> 1

# Consider input 12
#STEP 1-------------------------
#   1100  (n = 12)
# & 1011  (n - 1 = 11)
# ------
#   1000  (When i removed rightmost 1 the result is 8).

#STEP 2-------------------------
#   1000  (n = 8)
# & 0111  (n - 1 = 7)
# ------
#   0000  (The result is 0)