class Solution:
    def hammingWeight(self, n: int) -> int:
      count = 0
      while n != 0:
        # n % 2 is a way to read last digit in binary.
        # Example:
        # 1011 % 2 = 1
        # 1010 % 2 = 0
        if n % 2 == 1:
          count += 1
        # bitshift to the right
        n = n >> 1
      
      return count