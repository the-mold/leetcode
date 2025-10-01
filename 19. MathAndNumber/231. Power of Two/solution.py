class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False

        while n % 2 == 0:
            n /= 2
        
        return n == 1 # in the end n must be 1(because 2/2 above), if number is divisible by 2

# T:O(log n) because we divide number each step
# S:O(1)