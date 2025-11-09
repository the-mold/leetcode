class Solution:
    def countOnes(self, n):
        ans = 0
        while n != 0:
            ans += 1
            n = n & (n-1)
        return ans

    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for i, num in enumerate(nums):
            if self.countOnes(i) == k:
                ans += num
        return ans
      
# T:O(n * numberOfOnes)
# S:O(1)